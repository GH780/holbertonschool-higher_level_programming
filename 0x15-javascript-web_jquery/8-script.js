// Replaces value
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const list = data.results;
  for (let x = 0; x < list.length; x++) {
    $('#list_movies').append('<li>' + list[x].title + '<li>');
  }
});
