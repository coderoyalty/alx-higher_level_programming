#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  const len = list.length;
  for (let i = 0; i < len; i++) {
    if (searchElement === list[i]) {
      count += 1;
    }
  }
  return (count);
};
