#!/usr/bin/node

const arg = process.argv[2];

const fs = require('fs');

fs.readFile(arg, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
