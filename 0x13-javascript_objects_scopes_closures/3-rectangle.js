#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i, n, row;
    for (i = 0; i < this.height; i++) {
      row = '';
      for (n = 0; n < this.width; n++) {
        row += 'X';
      }
      console.log(row);
    }
  }
};
