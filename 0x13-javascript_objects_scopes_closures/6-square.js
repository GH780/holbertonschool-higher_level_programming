#!/usr/bin/node
const OldSquare = require('./5-square');

class Square extends OldSquare {
  charPrint (myChar) {
    if (myChar === undefined) {
      myChar = 'X';
    }
    let count;
    for (count = 0; count < this.height; count++) {
      console.log(myChar.repeat(this.width));
    }
  }
}
module.exports = Square;
