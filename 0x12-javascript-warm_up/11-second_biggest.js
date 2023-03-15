#!/usr/bin/node
// Script that searches the second biggest integer in the list of arguments.

function findSecondLargest (arr) {
  let largest = -Infinity;
  let secondLargest = -Infinity;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > largest) {
      secondLargest = largest;
      largest = arr[i];
    } else if (arr[i] > secondLargest && arr[i] < largest) {
      secondLargest = arr[i];
    }
  }
  return secondLargest;
}

const args = process.argv.slice(2);
const secondLargest = findSecondLargest(args.map(Number));

if (process.argv.length < 4 || process.argv.length === 3) {
  console.log(0);
} else {
  console.log(secondLargest);
}
