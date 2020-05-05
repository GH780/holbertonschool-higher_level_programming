#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  let count;
  for (count = 0; count < process.argv[2]; count++) {
    console.log('X'.repeat(process.argv[2]));
  }
}
