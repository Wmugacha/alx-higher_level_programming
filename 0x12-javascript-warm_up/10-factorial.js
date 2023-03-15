#!/usr/bin/node
// Script that computes and prints a factorial

function factorial (n) {
  if ((n === 0) || (isNaN(n))) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const arg = Number.parseInt(process.argv[2]);

console.log(factorial(arg));
