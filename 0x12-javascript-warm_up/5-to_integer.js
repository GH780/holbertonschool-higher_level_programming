#!/usr/bin/node
const list = [];
process.argv.forEach((val, index) => {
  if (index >= 2) {
    list.push(val);
  }
});
const number = parseInt(list[0], 10);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
