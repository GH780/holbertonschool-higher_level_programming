#!/usr/bin/node
const list = [];
process.argv.forEach((val, index) => {
  if (index >= 2) {
    list.push(val);
  }
});

console.log(list[0] + ' is ' + list[1]);
