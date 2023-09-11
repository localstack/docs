const fs = require('fs');
const path = require('path');

// This function converts a given string into a URL-friendly slug by
// replacing non-alphanumeric characters with hyphens, removing apostrophes,
// transliterating any non-ASCII characters to their closest ASCII equivalent,
// and converting all characters to lowercase.
// Usage: node create-applications.js

function slugify(str) {
  return str
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/[^a-zA-Z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '')
    .toLowerCase();
}

const applicationsFilePath = path.join(__dirname, '../data/developerhub/applications.json');
const destinationDirectory = path.join(__dirname, '../content/en/applications/');

const fileData = fs.readFileSync(applicationsFilePath, 'utf8');
const applications = JSON.parse(fileData).applications;

applications.forEach(application => {
  const slug = slugify(application.title);
  const tags = application.tags.map(tag => `- ${tag}`).join('\n');

  const folderPath = path.join(destinationDirectory, slug);
  fs.mkdirSync(folderPath, { recursive: true });

  const indexContent = `---
title: "${application.title}"
description: "${application.description}"
hide_feedback: true
hide_readingtime: true
type: applications
tags:
${tags}
---`;
  const indexPath = path.join(folderPath, 'index.md');
  fs.writeFileSync(indexPath, indexContent);
});