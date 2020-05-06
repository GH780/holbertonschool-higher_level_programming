#!/usr/bin/node
const array = [];
process.argv.forEach((val, index) => {
  if (index >= 2) {
    array.push(parseInt(val));
  }
});

function getNumber (list) {
  if (list.length === 0) return 0;
  if (list.length === 1) return 1;
  list.sort(function (a, b) {
    return a - b;
  });

  const max = Math.max.apply(null, list);

  const index = list.indexOf(max);
  if (index !== -1) {
    list.splice(index, 1);
  }
  return Math.max.apply(null, list);
}

console.log(getNumber(array));
