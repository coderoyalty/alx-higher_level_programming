#!/usr/bin/node

const argv = process.argv;
const value = Number(argv[2]);

if (isNaN(value)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < value; i++) {
    let line = '';
    for (let j = 0; j < value; j++) {
      line += 'X';
    }
    console.log(line);
  }
}
