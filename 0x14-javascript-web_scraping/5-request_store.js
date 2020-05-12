#!/usr/bin/node
const request = require('request');
const modFs = require('fs');
request(process.argv[2], 'utf-8', (error, response, body) => {
  if (error) { console.log(error); } else {
    modFs.writeFile(process.argv[3], body, (err) => {
      if (err) { console.log(err); }
    });
  }
});
