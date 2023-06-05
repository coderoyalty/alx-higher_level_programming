#!/usr/bin/node

const request = require('request');
const argv = process.argv;
const url = 'https://swapi-api.alx-tools.com/api/films';
const id = argv[2];
request.get(`${url}/${id}`, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }
  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
