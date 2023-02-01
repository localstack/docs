#!/bin/bash
set -euo pipefail

# input params
PARENT_FOLDER=${1:-target}
METRICS_ARTIFACTS_BRANCH=${2:-master}
REPOSITORY_NAME=${REPOSITORY_NAME:-localstack-ext}
ARTIFACT_ID=${ARTIFACT_ID:-parity-metric-ext-raw}
WORKFLOW=${WORKFLOW:-"Integration Tests"}
RENAME_ARTIFACT=${RENAME_ARTIFACT:-pro-integration-test.csv}

REPOSITORY_OWNER=localstack
METRICS_RAW="$PARENT_FOLDER/metrics-raw"

TMP_FOLDER=$PARENT_FOLDER/tmp_download
mkdir -p $TMP_FOLDER

echo "Searching for Artifact: $ARTIFACT_ID on branch $METRICS_ARTIFACTS_BRANCH in repo $REPOSITORY_OWNER/$REPOSITORY_NAME."

# Get the latest successful build
RUN_ID=$(gh run list --limit 1 --branch $METRICS_ARTIFACTS_BRANCH --repo $REPOSITORY_OWNER/$REPOSITORY_NAME --workflow $WORKFLOW --json databaseId,conclusion --jq '.[] | select(.conclusion=="success")' | jq -r .databaseId)
echo "Trying to download file with runid $RUN_ID..."

# we do not want to exit if this command fails -> using or true
gh run download $RUN_ID --repo $REPOSITORY_OWNER/$REPOSITORY_NAME -n $ARTIFACT_ID -D $TMP_FOLDER || true

# count the files with the pattern (we do not know the exact name) to check if we downloaded something
if [ 0 -lt $(ls $TMP_FOLDER 2>/dev/null | wc -w) ]; then
    echo "...downloaded $ARTIFACT_ID successfully."
else 
    # runs on master often do NOT run the parity tests! we need to take the PR build which caused the master build to be skipped
    # this one will have the same tree_id hash
    echo "...download did not succeed, searching for build that created the artifact."
    
    # first find the tree_id from the RUN_ID we are interested in
    DETAILS=$(gh api repos/$REPOSITORY_OWNER/$REPOSITORY_NAME/actions/runs/$RUN_ID |  jq -r '{id, tree_id: .head_commit.tree_id, head_branch, created_at}')
    echo "RUN_ID details: $DETAILS"

    TREE_ID=$(echo $DETAILS | jq -r .tree_id)
    CREATED=$(echo $DETAILS | jq -r .created_at)

    # now search for runs with the same tree_id but different run_id
    # by default returns 30 builds, which should be enough, given we also filter for created and status
    RELATED_BUILD_DETAILS=$(gh api -XGET repos/$REPOSITORY_OWNER/$REPOSITORY_NAME/actions/runs -F status='success' -F created="<$CREATED" \
                            | jq -r .workflow_runs | jq -r '.[] | {id, tree_id: .head_commit.tree_id, head_branch}' \
                            | jq --arg TREE_ID $TREE_ID --arg RUN_ID $RUN_ID -c 'select( .id != $RUN_ID and .tree_id == $TREE_ID)')
    
    echo "Found related build details: $RELATED_BUILD_DETAILS"

    RELATED_ID=$(echo $RELATED_BUILD_DETAILS | jq -rs '.[0].id')
    echo "Extracted ID $RELATED_ID, trying to download artefacts now..."

    # download the artifact for the realted build
    gh run download $RELATED_ID --repo $REPOSITORY_OWNER/$REPOSITORY_NAME -n $ARTIFACT_ID -D $TMP_FOLDER || true
    
    # count the files with the pattern (we do not know the exact name) to check if we downloaded something
    if [ 0 -lt $(ls $TMP_FOLDER 2>/dev/null | wc -w) ]; then
        echo "...downloaded $ARTIFACT_ID successfully."
    else 
        # in case this failed as well, fallback to download latest artifact from that repo
        echo "Download failed again, falling back to downloading the latest artifact.."
        gh run download --repo $REPOSITORY_OWNER/$REPOSITORY_NAME -n $ARTIFACT_ID
    fi
fi


echo "Moving raw metrics data to $METRICS_RAW"
mkdir -p $METRICS_RAW
mv $TMP_FOLDER/*.csv $METRICS_RAW/$RENAME_ARTIFACT
rm -rf $TMP_FOLDER
echo "Done."