#!/usr/bin/node

const argv = process.argv;

let secondBiggest = 0;

if (argv.length > 3) {
  let first = argv[2];
  let second = Number.MIN_VALUE;

  for (let i = 2; i < argv.length; i++) {
    const current = argv[i];
    if (current > first) {
      second = first;
      first = current;
    } else if (current > second && current < first) { second = current; }
  }
  secondBiggest = second;
}

console.log(secondBiggest);
