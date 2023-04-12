#!/usr/bin/node

const argv = process.argv;
const fs = require('fs');
const firstContent = fs.readFileSync(`./${argv[2]}`);
const secondContent = fs.readFileSync(`./${argv[3]}`);
const content = firstContent + secondContent;
fs.writeFileSync(`./${argv[4]}`, content);
