#!/usr/bin/node

const _Square = require('./5-square');

class Square extends _Square {
  charPrint (val) {
    if (val) {
      for (let i = 0; i < this.height; i++) {
        let line = '';
        for (let j = 0; j < this.width; j++) {
          line += val;
        }
        console.log(line);
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
