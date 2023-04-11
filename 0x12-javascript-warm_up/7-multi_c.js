#!/usr/bin/node

const argv = process.argv;
const value = Number(argv[2]);

if (isNaN(value)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < value; i++) {
    console.log('C is fun');
  }
}
