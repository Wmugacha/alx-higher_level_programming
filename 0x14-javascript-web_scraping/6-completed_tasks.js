#!/usr/bin/node
// Script that computes the number of tasks completed by user id.

const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) console.error(err);
  const tasks = JSON.parse(body);
  const dict = {};
  for (let i = 0; i < tasks.length; i++) {
    if (tasks[i].completed) {
      if (dict[tasks[i].userId] === undefined) {
        dict[tasks[i].userId] = 1;
      } else {
        dict[tasks[i].userId]++;
      }
    }
  }
  console.log(dict);
});
