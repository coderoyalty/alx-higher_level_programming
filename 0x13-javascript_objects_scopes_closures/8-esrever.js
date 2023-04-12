#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  const listLength = list.length;

  for (let i = listLength - 1; i >= 0; i--) {
    const item = list[i];
    reversedList.push(item);
  }

  return (reversedList);
};
