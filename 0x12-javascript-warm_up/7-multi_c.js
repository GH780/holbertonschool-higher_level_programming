#!/usr/bin/node
let len = 0;
process.argv.forEach((val, index) => {
  if (index === 2) {
    let x;
    for (x = 0; x < val; x++) {
      console.log('C is fun');
    }
  }
  len = index;
});

if (len < 2) {
  console.log('Missing number of occurrences');
}
