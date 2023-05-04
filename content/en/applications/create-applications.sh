#!/bin/sh

# Example usage
# bash create-applications.sh ../../../data/developerhub/applications.json

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