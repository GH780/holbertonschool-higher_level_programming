#!/usr/bin/node
const request = require('request');
const request2 = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url + process.argv[2], (error, response, body) => {
  if (error) { console.log(error); } else {
    const listCharacters = JSON.parse(body).characters;
    for (let y = 0; y < listCharacters.length; y++) {
      request2(listCharacters[y], (error, response, body) => {
        if (error) { console.log(error); } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
