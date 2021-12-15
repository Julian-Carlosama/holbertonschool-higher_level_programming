#!/usr/bin/node
const square5 = require('./5-square');
class Square extends square5 {
  charPrint (c) {
    if (c === undefined) {
      //    c = 'X';
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let squ = '';
        for (let j = 0; j < this.width; j++) {
          squ += 'C';
        }
        console.log(squ);
      }
    }
  }
}
module.exports = Square;
