---
title: "LocalStack Coverage"
linkTitle: "LocalStack Coverage"
weight: 5
description: >
  Overview of the implemented AWS APIs in LocalStack
cascade:
  type: docs
aliases:
  # TODO this one links to the feature coverage 
  # - /localstack/coverage/
  - /references/coverage/
hide_feedback: true
hide_readingtime: true
---
<script>
function searchForServiceNameInLink() {
  var input, filter, div, elements, a, i, txtValue;
  input = document.getElementById('serviceNameCoverageInput');
  filter = input.value.toUpperCase();
  div = document.getElementsByClassName['section-index'](0)
  elements = div.getElementsByClassName('entry');

  // Loop through all list items, and hide those who don't match the search query
  for (i = 0; i < elements.length; i++) {
    textContent = elements[i].innerText;
    if (textContent.toUpperCase().indexOf(filter) > -1) {
      elements[i].style.display = "inline";
    } else {
      elements[i].style.display = "none";
    }
  }
}
</script>

<input autocomplete=off type="text" id="serviceNameCoverageInput" onkeyup="searchForServiceNameInLink()" placeholder="🔍 Search for Service Name ...">

<!-- this div is used as a reference point of where to apply custom style to the list of subcontent -->
<div id="coverage-page"></div>
