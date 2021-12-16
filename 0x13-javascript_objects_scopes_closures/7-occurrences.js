#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let numOcu = 0;

  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      numOcu += 1;
    }
  }
  return (numOcu);
};
