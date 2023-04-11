#!/usr/bin/node

const argv = process.argv;

function factorial (num) {
  const val = Number(num);
  if (isNaN(val)) {
    return (1);
  } else if (val === 1) {
    return (1);
  } else {
    return (val * factorial(val - 1));
  }
}

console.log(factorial(argv[2]));
