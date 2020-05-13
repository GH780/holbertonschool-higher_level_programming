#!/usr/bin/node
const request = require('request');
const tasks = {};
request(process.argv[2], (error, response, body) => {
  if (error) { console.log(error); } else {
    const list = JSON.parse(body);
    for (let x = 0; x < list.length; x++) {
      if (!(list[x].userId in tasks)) {
        tasks[list[x].userId] = 0;
      }
      if (list[x].completed === true) {
        tasks[list[x].userId] = tasks[list[x].userId] + 1;
      }
    }
    console.log(tasks);
  }
});
