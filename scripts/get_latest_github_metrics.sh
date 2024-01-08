#!/bin/bash
set -euo pipefail

# input params
PARENT_FOLDER=${1:-target}
METRICS_ARTIFACTS_BRANCH=${2:-master}

# ENVs
REPOSITORY_NAME=${REPOSITORY_NAME:-localstack-ext}
ARTIFACT_ID=${ARTIFACT_ID:-parity-metric-ext-raw}
WORKFLOW=${WORKFLOW:-"Integration Tests"}
PREFIX_ARTIFACT=${PREFIX_ARTIFACT:-}
FILTER_SUCCESS=${FILTER_SUCCESS:-1}

RESOURCE_FOLDER=${RESOURCE_FOLDER:-metrics-raw}
REPOSITORY_OWNER=localstack
TARGET_FOLDER="$PARENT_FOLDER/$RESOURCE_FOLDER"

TMP_FOLDER=$PARENT_FOLDER/tmp_download
mkdir -p $TMP_FOLDER

# Resulting directory structure required for the create_data_coverage.py
# - resources/metrics-raw
#   - community-integration-test.csv (Community)
#   - pro-integration-test.csv (Pro)              -> fetched from GitHub
#   - moto-integration-test.csv (Moto)            -> fetched from GitHub
#   - ...
# - resources/metrics-implementation-details
#   - community
#     - implementation_coverage_full.csv
#   - pro
#     - implementation_coverage_full.csv          -> fetched from GitHub

echo "Searching for Artifact: $ARTIFACT_ID in workflow '$WORKFLOW' on branch $METRICS_ARTIFACTS_BRANCH in repo $REPOSITORY_OWNER/$REPOSITORY_NAME."

# Get the latest successful build
# check filter criteria - some workflows might be expected to fail, but still have the artifact we are interested in
if [ "$FILTER_SUCCESS" == "1" ]; then
    echo "searching last workflow with 'conclusion=success'"
    RUN_ID=$(gh run list --limit 20 --branch $METRICS_ARTIFACTS_BRANCH --repo $REPOSITORY_OWNER/$REPOSITORY_NAME --workflow "$WORKFLOW" --json databaseId,conclusion,status --jq '.[] | select(.conclusion=="success")' | jq -rs '.[0].databaseId')
else
    echo "searching last workflow with 'status=completed'"
    RUN_ID=$(gh run list --limit 20 --branch $METRICS_ARTIFACTS_BRANCH --repo $REPOSITORY_OWNER/$REPOSITORY_NAME --workflow "$WORKFLOW" --json databaseId,conclusion,status --jq '.[] | select(.status=="completed" and (.conclusion=="failure" or .conclusion=="success"))' | jq -rs '.[0].databaseId')
fi

if [ "$RUN_ID" == "null" ];then
    echo "no run id found something must be wrong, exiting now..."
    exit 1
fi

echo "Trying to download file with runid $RUN_ID..."

# we do not want to exit if this command fails -> using or true
gh run download $RUN_ID --repo $REPOSITORY_OWNER/$REPOSITORY_NAME -p "$ARTIFACT_ID" -D $TMP_FOLDER || true

# count the files with the pattern (we do not know the exact name) to check if we downloaded something
if [ 0 -lt $(ls $TMP_FOLDER 2>/dev/null | wc -w) ]; then
    echo "...downloaded $ARTIFACT_ID successfully."
    tree $TMP_FOLDER
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

    # download the artifact for the related build -> this time we fail if the download was not successful
    gh run download $RELATED_ID --repo $REPOSITORY_OWNER/$REPOSITORY_NAME -n $ARTIFACT_ID -D $TMP_FOLDER
    echo "...dowloaded $ARTIFACT_ID successfully"
    tree $TMP_FOLDER
fi


echo "Moving artifact to $TARGET_FOLDER"
mkdir -p $TARGET_FOLDER
if [[ -z "${PREFIX_ARTIFACT}" ]]; then
    # pro implementation_coverage artifact download has a subfolder "pro"
    cp -R $TMP_FOLDER/**/* $TARGET_FOLDER
else
    # metrics-raw-data artifacts -> we are only want to keept the csv and rename it
    for file in $TMP_FOLDER/**/*.csv; do
      org_file_name=$(echo $file | sed "s/.*\///")
      mv -- "$file" "$TARGET_FOLDER/$PREFIX_ARTIFACT-$org_file_name"
    done
fi

# cleanup
rm -rf $TMP_FOLDER
echo "content of $TARGET_FOLDER:"
tree $TARGET_FOLDER
echo "Done."