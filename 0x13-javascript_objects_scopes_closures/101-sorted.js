#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};

for (let key in dict) {
    const val = dict[key];
    if (newDict[val] === undefined) {
        newDict[val] = []
    }
    newDict[val].push(key)
}

console.log(newDict);

