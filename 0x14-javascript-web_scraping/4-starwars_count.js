#!/usr/bin/node
const request = require('request');
let count = 0;
request(process.argv[2], (error, response, body) => {
  if (error) { console.log(error); } else {
    const listFilm = JSON.parse(body).results;
    for (let x = 0; x < listFilm.length; x++) {
      const listCharacters = listFilm[x].characters;
      for (let y = 0; y < listCharacters.length; y++) {
        if (listCharacters[y].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
