#!/bin/bash
set -euo pipefail

# input params
PARENT_FOLDER=${1:-target}
METRICS_ARTIFACTS_BRANCH=${2:-master}

# parameterization
PROJECT_SLUG="github/localstack/localstack"
METRICS_RAW="$PARENT_FOLDER/metrics-raw/"
METRICS_IMPL="$PARENT_FOLDER/metrics-implementation-details/"

# Resulting directory structure required for the create_data_coverage.py
# - resources/metrics-raw
#   - community-integration-test.csv (Community) -> this is downloaded from CircleCI (using this script)
#   - pro-integration-test.csv (Pro)
#   - moto-integration-test.csv (Moto)
#   - ...
# - resources/metrics-implementation-details
#   - community
#     - implementation_coverage_full.csv -> this is downloaded from CircleCI (using this script)
#   - pro
#     - implementation_coverage_full.csv

echo "Project: $PROJECT_SLUG."

WORKFLOW_ID=$(curl -X 'GET' "https://circleci.com/api/v2/insights/${PROJECT_SLUG}/workflows/main?branch=${METRICS_ARTIFACTS_BRANCH}" -H 'accept: application/json' | jq -r '[.items[] | select(.status == "success")][0].id')
echo "Latest successful workflow: $WORKFLOW_ID"

JOB_NUMBER=$(curl -X 'GET' "https://circleci.com/api/v2/workflow/${WORKFLOW_ID}/job" -H 'accept: application/json'| jq -r '.items[] | select(.name == "report") | .job_number')
echo "Report job number: $JOB_NUMBER"

ARTIFACT_URLS=$(curl -X 'GET' "https://circleci.com/api/v2/project/${PROJECT_SLUG}/${JOB_NUMBER}/artifacts" -H 'accept: application/json' -H "Circle-Token:${CIRCLE_CI_TOKEN}" | jq -r '.items[] | select(.url | endswith(".csv")) | .url')
echo "Raw metrics data URLs:"
echo "$ARTIFACT_URLS"

echo "Downloading metrics data..."
wget -m --cut-dirs 5 --no-host-directories $ARTIFACT_URLS --header "Circle-Token: ${CIRCLE_CI_TOKEN}"

echo "Moving raw community metrics data to $METRICS_RAW"
mkdir -p $METRICS_RAW
for file in parity_metrics/*.csv; do
      org_file_name=$(echo $file | sed "s/.*\///")
      mv -- "$file" "$METRICS_RAW/community-integration-test-$org_file_name"
done


echo "Moving community metrics implementation details to $METRICS_IMPL..."
mkdir -p $METRICS_IMPL
mv community $METRICS_IMPL

# TODO might change in the future
echo "Deleting acceptance_parity_metrics for now (currently subset of parity_metrics)"
rm -rf acceptance_parity_metrics

echo "Resulting file structure:"
tree $PARENT_FOLDER

echo "Done."