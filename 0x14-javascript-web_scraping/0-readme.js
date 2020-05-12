#!/usr/bin/node
const modFs = require('fs');
modFs.readFile(process.argv[2], 'utf-8', function (err, data) {
  if (err) throw err;
  console.log(data);
});
