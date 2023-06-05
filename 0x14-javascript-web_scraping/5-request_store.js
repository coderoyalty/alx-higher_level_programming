#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const argv = process.argv;
const url = argv[2];
const filePath = argv[3];

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  if (response.statusCode !== 200) {
    return;
  }

  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
