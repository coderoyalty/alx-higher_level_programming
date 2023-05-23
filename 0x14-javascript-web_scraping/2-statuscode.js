#!/usr/bin/node

const request = require('request');
const argv = process.argv;

const url = argv[2];
request.get(url, (err, response, body) => {
    if (err) {
        console.error(err);
        return;
    }
    else {
        console.log("code: " + response.statusCode);
        return;
    }
})
