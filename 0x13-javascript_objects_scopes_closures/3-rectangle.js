#!/usr/bin/node
class Rectangle {
  constructor (width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    let count;
    for (count = 0; count < this.height; count++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
