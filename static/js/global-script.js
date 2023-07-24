function codeCopyBtnClickHandler(){
  $('.code-copy-button').on('click',function(e){
    e.preventDefault();
    const elem = $(this).closest('.code-container').find('code').clone();
    elem.find('.command-prefix').remove(); // removing prefix
    navigator.clipboard.writeText(elem.text());
    $(this).find('span').text('Copied!');
    setTimeout(() => {
      $(this).find('span').text('Copy');
    }, 2000);
  })
}

$('.highlight pre').each(function(_i,item){
  $(item).addClass('code-container');
  $(item).append('<button class="code-copy-button"><i class="fa fa-copy"></i><span>Copy</span></button>')
})
codeCopyBtnClickHandler();
