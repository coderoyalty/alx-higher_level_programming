#!/usr/bin/node

argv = process.argv;
const fs = require('fs');

const filePath = argv[2];
const content = argv[3];

fs.writeFile(filePath, content, "utf-8", (err) => {
    if (err) {
        console.error(err)
    }
})
