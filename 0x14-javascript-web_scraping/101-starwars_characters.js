#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const listUrl = [];
request(url + process.argv[2], (error, response, body) => {
  if (error) { console.log(error); } else {
    const listCharacters = JSON.parse(body).characters;
    for (let y = 0; y < listCharacters.length; y++) {
      listUrl.push(listCharacters[y]);
    }
    printNames(0, listUrl[0], listCharacters, listCharacters.length);
  }
});

function printNames (x, url, listUrl, size) {
  if (x === (size)) { return; }
  request(listUrl[x], (error, response, body) => {
    if (error) { console.log(error); } else {
      console.log(JSON.parse(body).name);
      x++;
      printNames(x, listUrl[x], listUrl, size);
    }
  });
}
