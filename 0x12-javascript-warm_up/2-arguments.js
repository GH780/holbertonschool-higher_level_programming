#!/usr/bin/node
let len = 0;
process.argv.forEach((val, index) => {
  len = index;
});

if (len === 2) {
  console.log('Argument found');
} else if (len > 2) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
