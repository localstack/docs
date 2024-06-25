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
LIMIT=${LIMIT:-20}

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
    SELECTOR='.[] | select(.conclusion=="success")'
else
    echo "searching last workflow with 'status=completed'"
    SELECTOR='.[] | select(.status=="completed" and (.conclusion=="failure" or .conclusion=="success"))'
fi
RUN_IDS=$(gh run list --limit $LIMIT --branch $METRICS_ARTIFACTS_BRANCH --repo $REPOSITORY_OWNER/$REPOSITORY_NAME --workflow "$WORKFLOW" --json databaseId,conclusion,status --jq "$SELECTOR")

if [ $( echo $RUN_IDS | jq -rs '.[0].databaseId' ) == "null" ];then
    echo "no run id found something must be wrong, exiting now..."
    exit 1
fi

for (( i=0; i<$LIMIT; i++ )); do
  # Extract the element at index $i
  RUN_ID=$(echo $RUN_IDS | jq -rs ".[$i].databaseId")
  echo "Trying to download file with run_id $RUN_ID..."

  # we do not want to exit if this command fails -> using or true
  gh run download $RUN_ID --repo $REPOSITORY_OWNER/$REPOSITORY_NAME -p "$ARTIFACT_ID" -D $TMP_FOLDER || true

  # check if something got downloaded and break out of loop if so
  if [ 0 -lt $(ls $TMP_FOLDER 2>/dev/null | wc -w) ]; then
    echo "Downloaded $ARTIFACT_ID successfully!"
    tree $TMP_FOLDER
    break
  fi
done


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
