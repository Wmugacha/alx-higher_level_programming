#!/usr/bin/node

// Print first argument passed to the script

if (process.argv[2] !== undefined) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
