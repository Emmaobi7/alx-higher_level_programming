#!/usr/bin/node

const Parent = require('./5-square');

class Square extends Parent {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let i;
      for (i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
