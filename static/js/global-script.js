function setupCodeBlockCopyButton() {
  $('.highlight pre').each(function (_i, item) {
    $(item).addClass('code-container');
    $(item).append('<button class="code-copy-button"><i class="fa fa-copy"></i><span>Copy</span></button>')
  })

  $('.code-copy-button').on('click', function (e) {
    e.preventDefault();
    const elem = $(this).closest('.code-container').find('code').clone();
    elem.find('.command-prefix').remove(); // removing prefix
    elem.find('.disable-copy').remove(); // removing text which shouldn't be copied
    navigator.clipboard.writeText(elem.text().trim());
    $(this).find('span').text('Copied!');
    setTimeout(() => {
      $(this).find('span').text('Copy');
    }, 2000);
  })
}

function playYoutubeVideo() {
  $('.video-thumbnail').on('click', function () {
    var url = $(this).attr('data-url');
    var iframeHtml = '<iframe width="100%" src="' + url + '?autoplay=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
    $(this).append(iframeHtml)
    $(this).addClass('played');
  })
}

setupCodeBlockCopyButton();
playYoutubeVideo();
