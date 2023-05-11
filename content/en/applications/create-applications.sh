#!/bin/sh

# Example usage
# bash create-applications.sh ../../../data/developerhub/applications.json
# Dependencies for this script: jq

# This function converts a given string into a URL-friendly slug by
# replacing non-alphanumeric characters with hyphens, removing apostrophes,
# transliterating any non-ASCII characters to their closest ASCII equivalent,
# and converting all characters to lowercase.
function slugify() {
  iconv -t ascii//TRANSLIT \
  | tr -d "'" \
  | sed -E 's/[^a-zA-Z0-9]+/-/g' \
  | sed -E 's/^-+|-+$//g' \
  | tr "[:upper:]" "[:lower:]"
}
if [[ $# -eq 0 ]] ; then
    echo 'Please pass path argument'
    exit 0
fi
APPLICATIONS=$(jq '.applications' $1)

# The loop iterates applications array encoded in base64 format to avoid special characters.
# The data is decoded back to its original JSON format and data is extracted using jq.
# A slug is created from the title, and a folder is created with the slug as the folder name.
# An index.md file is created inside the folder,
# which contains the application information extracted earlier.
for row in $(echo "${APPLICATIONS}" | jq -r '.[] | @base64'); do
    _jq() {
     echo ${row} | base64 --decode | jq -r ${1}
    }
   SLUG=$(_jq '.title' | slugify)
   TAGS=$(_jq '.tags')
   for i in $(echo "${TAGS}" | jq -r '.[] | @base64'); do
      TAGS_STRING=$TAGS_STRING"- "$(echo $i | base64 --decode)"\n"
   done
   mkdir -p $SLUG
   echo -e \
'---
title: "'$(_jq '.title')'"
description: '$(_jq '.description')'
hide_feedback: true
hide_readingtime: true
type: applications
tags:
'$TAGS_STRING'---'\
> $SLUG/index.md
done