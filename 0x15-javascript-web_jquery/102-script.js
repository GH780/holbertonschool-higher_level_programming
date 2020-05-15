// Using API to translate hello
window.addEventListener('load', function () {
  $('#btn_translate').click(function () {
    const url = 'https://fourtonfish.com/hellosalut/?lang=';
    $.get(url + $('#language_code').val(), function (data) {
      $('#hello').text(data.hello);
    });
  });
});
