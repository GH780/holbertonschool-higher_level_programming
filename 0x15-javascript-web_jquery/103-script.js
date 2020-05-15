// Using API to translate hello
window.addEventListener('load', function () {
  $('#btn_translate').click(function () {
    translate();
  });

  $('#language_code').keypress(function (event) {
    var keycode = (event.keyCode ? event.keyCode : event.which);
    if (keycode === '13') {
      translate();
    }
  });
});

function translate () {
  const url = 'https://fourtonfish.com/hellosalut/?lang=';
  $.get(url + $('#language_code').val(), function (data) {
    $('#hello').text(data.hello);
  });
}
