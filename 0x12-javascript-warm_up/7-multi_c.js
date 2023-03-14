#!/usr/bin/node
// Print the first argument x number of times

const x = Number.parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let step = 0; step < x; step++) {
    console.log('C is fun');
  }
}
