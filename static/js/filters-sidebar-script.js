var $items = $(".filters-card");
var $noResults = $("#no-results");
var $clearFiltersBtn = $(".clear-filters-btn");
var $showAllAppsBtn = $("#show-all-apps-btn");
var $sidebarFiltersParent = $('#sidebar-filters-parent');
var filtersSidebarLabels = {
  services: 'Services',
  deployments: 'Infrastructure Provisioned',
  platforms: 'Programming language',
  levels: 'Complexity',
  cloudpods: 'Cloud Pods',
}
var filtersState = {
  services: [],
  deployments: [],
  platforms: [],
  levels: [],
  cloudpods: [],
};

var levelsSorter = function (a, b) {
  let levelOrder = filtersConfig.levelOrder;
  // Required as its custom sorting
  return levelOrder.indexOf(a) - levelOrder.indexOf(b);
};

var generateCheckboxItemHtml = function (prefix, lookup, item) {
  return `
      <div class="custom-control custom-checkbox">
        <input type="checkbox" value="${prefix}-${item}" class="custom-control-input" id="${prefix}-${item}" aria-label="${prefix}-${item}">
        <label class="custom-control-label" for="${prefix}-${item}">${lookup[item] || item}</label>
      </div>
      `;
};
var generateFiltersGroupHtml = function (name, checkboxesHtml) {
  $sidebarFiltersParent.append(`
      <div class="filters-group">
        <h6>${filtersSidebarLabels[name]}</h6>
        <div id="filter-${name}-container">${checkboxesHtml}</div>
      </div>
  `);
}
var generateCloudPodsFiltersGroupHtml = function () {
  $sidebarFiltersParent.append(`
<div class="filters-group">
    <h6>${filtersSidebarLabels['cloudpods']}</h6>
    <div id="filter-cloudpods-container">
      <div class="custom-control custom-checkbox">
        <input type="checkbox" value="cloudpod-true" class="custom-control-input" id="cloudpod-checkbox" aria-label="cloudpod-checkbox" />
        <label class="custom-control-label" for="cloudpod-checkbox">Yes</label>
      </div>
    </div>
  </div>
`)
};

var buildFiltersUI = function () {
  let services = "";
  let deployments = "";
  let platforms = "";
  let levels = "";

  $items.each(function (_i, value) {
    let service = value.getAttribute("data-services");
    let platform = value.getAttribute("data-platforms");
    let deployment = value.getAttribute("data-deployments");
    let level = value.getAttribute("data-levels");

    services += service ? service.split(",") + "," : "";
    platforms += platform ? platform.split(",") + "," : "";
    deployments += deployment ? deployment.split(",") + "," : "";
    levels += level ? level.split(",") + "," : "";
  });

  // Set removes duplicates
  services = Array.from(new Set(services.slice(0, -1).split(",")));
  platforms = Array.from(new Set(platforms.slice(0, -1).split(",")));
  deployments = Array.from(new Set(deployments.slice(0, -1).split(",")));
  levels = Array.from(new Set(levels.slice(0, -1).split(",")));

  let servicesHtml = "";
  let deploymentsHtml = "";
  let platformsHtml = "";
  let levelsHtml = "";

  if (services[0]) {
    services.sort().map(function (service) {
      servicesHtml += generateCheckboxItemHtml("service", filtersConfig.data.services, service);
    });
    generateFiltersGroupHtml('services', servicesHtml);
  }
  if (deployments[0]) {
    deployments.sort().map(function (deployment) {
      deploymentsHtml += generateCheckboxItemHtml("deployment", filtersConfig.data.deployments, deployment);
    });
    generateFiltersGroupHtml('deployments', deploymentsHtml);
  }
  if (platforms[0]) {
    platforms.sort().map(function (platform) {
      platformsHtml += generateCheckboxItemHtml("platform", filtersConfig.data.platforms, platform);
    });
    generateFiltersGroupHtml('platforms', platformsHtml);
  }
  if (levels[0]) {
    levels.sort(levelsSorter).map(function (level) {
      levelsHtml += generateCheckboxItemHtml("level", filtersConfig.data.levels, level);
    });
    generateFiltersGroupHtml('levels', levelsHtml);
  }
  if (filtersConfig.hasCloudPod) generateCloudPodsFiltersGroupHtml();
};

var bindFilterEvents = function () {
  var $filterCheckboxes = $("#sidebar-filters-parent .custom-control-input");

  $clearFiltersBtn.on("click", function () {
    filtersState = Object.keys(filtersState).reduce(function (acc, item) {
      return Object.assign(acc, { [item]: [] })
    }, {})
    $('aside').find($clearFiltersBtn).hide();
    $filterCheckboxes.prop("checked", false);
    updateApplicationsUI();
  });
  $filterCheckboxes.on("change", function (e) {
    let type = `${e.target.value.split("-")[0]}s`;
    let arr = e.target.checked
      ? filtersState[type].concat(e.target.value)
      : filtersState[type].filter(function (item) {
        return item !== e.target.value;
      });
    Object.assign(filtersState, { [type]: arr });
    updateApplicationsUI();
  });
};

var isFiltersApplied = function () {
  let applied = false;
  Object.keys(filtersState).forEach(function (key) {
    if (filtersState[key].length !== 0) applied = true;
  });
  return applied;
};

var updateApplicationsUI = function () {
  $noResults.hide();

  if (!isFiltersApplied()) {
    $('aside').find($clearFiltersBtn).hide();
    $items.show();
    return;
  }

  $items.hide();
  $clearFiltersBtn.show();

  var $filteredItems = $items;
  Object.keys(filtersState).forEach(function (key) {
    let selector = filtersState[key].length === 1 ? filtersState[key][0] : filtersState[key].join(".");
    $filteredItems = $filteredItems.filter(selector !== "" ? `.${selector}` : "*");
  });
  $filteredItems.show();
  if ($filteredItems.length === 0) $noResults.show();
};

var filterByQueryString = function () {
  let queryString = window.location.search;
  let urlParams = new URLSearchParams(queryString);
  let id = urlParams.get("id");
  if (!id || !$(`[data-slug="${id}"]`).length) return;
  $items.not(`[data-slug="${id}"]`).hide();
  $showAllAppsBtn.show();
  $showAllAppsBtn.on('click', function () {
    $(this).remove();
    $items.show();
  })
};

buildFiltersUI();
bindFilterEvents();
filterByQueryString();