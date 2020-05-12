#!/usr/bin/node
const modFs = require('fs');
modFs.writeFile(process.argv[2], process.argv[3], (err) => {
  if (err) { console.log(err); }
});
