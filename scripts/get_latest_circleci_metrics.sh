#!/bin/bash
set -euo pipefail

# input params
PARENT_FOLDER=${1:-target}
METRICS_ARTIFACTS_BRANCH=${2:-master}

# parameterization
PROJECT_SLUG="github/localstack/localstack"
METRICS_RAW="$PARENT_FOLDER/metrics-raw/"
METRICS_IMPL="$PARENT_FOLDER/metrics-implementation-details"
METRICS_IMPL_COMMUNITY="$METRICS_IMPL/community/"
METRICS_IMPL_PRO="$METRICS_IMPL/pro/"

echo "Project: $PROJECT_SLUG."

WORKFLOW_ID=$(curl -X 'GET' "https://circleci.com/api/v2/insights/${PROJECT_SLUG}/workflows/main?branch=${METRICS_ARTIFACTS_BRANCH}" -H 'accept: application/json' | jq -r '[.items[] | select(.status == "success")][0].id')
echo "Latest successful workflow: $WORKFLOW_ID"

JOB_NUMBER=$(curl -X 'GET' "https://circleci.com/api/v2/workflow/${WORKFLOW_ID}/job" -H 'accept: application/json' | jq -r '.items[] | select(.name == "report") | .job_number')
echo "Report job number: $JOB_NUMBER"

ARTIFACT_URLS=$(curl -X 'GET' "https://circleci.com/api/v2/project/${PROJECT_SLUG}/${JOB_NUMBER}/artifacts" -H 'accept: application/json' | jq -r '.items[] | select(.url | endswith(".csv")) | .url')
echo "Raw metrics data URLs:"
echo "$ARTIFACT_URLS"

echo "Downloading metrics data..."
wget $ARTIFACT_URLS

# Create the following directory structure for the coverage_docs_utility.py
# - resources/metrics-raw
#   - metric-report-raw-data-2022-08-16__11_37_31-d1e519d6.csv (Pro)
#   - metric-report-raw-data-2022-08-16__11_37_31-d1e51as6.csv (Community)
# - resources/metrics-implementation-details
#   - pro
#     - implementation_coverage_full.csv
#   - community
#     - implementation_coverage_full.csv

echo "Moving raw community metrics data to $METRICS_RAW"
mkdir -p $METRICS_RAW
mv metrics-report-*.csv $METRICS_RAW

echo "Moving community metrics implementation details to $METRICS_IMPL_COMMUNITY..."
# TODO check if this file name is correct
mv community_implementation_coverage_full.csv $METRICS_IMPL_COMMUNITY

echo "Moving pro metrics implementation details to $METRICS_IMPL_PRO..."
# TODO check if this file name is correct
mv pro_implementation_coverage_full.csv $METRICS_IMPL_PRO

echo "Resulting file structure:"
tree $PARENT_FOLDER

echo "Done."