#!/usr/bin/node

const argv = process.argv;
const noArg = argv.length;
let message = '';

if (noArg === 2) {
  message = 'No argument';
} else if (noArg === 3) {
  message = 'Argument found';
} else {
  message = 'Arguments found';
}

console.log(message);
