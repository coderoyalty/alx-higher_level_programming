#!/usr/bin/node

const argv = process.argv;
const value = Number(argv[2]);

if (isNaN(value)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${value}`);
}
