#!/usr/bin/node
let len = 0;
process.argv.forEach((val, index) => {
  if (index === 2) {
    console.log(val);
  }
  len = index;
});

if (len < 2) {
  console.log('No argument');
}
