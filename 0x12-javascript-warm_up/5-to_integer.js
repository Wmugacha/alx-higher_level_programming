#!/usr/bin/node
// Convert first argument to an integer

const arg1 = Number.parseInt(process.argv[2]);

if (isNaN(arg1)) {
  console.log('Not a number');
} else {
  console.log('My number:', arg1);
}
