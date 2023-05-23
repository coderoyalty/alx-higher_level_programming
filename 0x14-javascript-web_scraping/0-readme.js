#!/usr/bin/node

const fs = require('fs')
const argv = process.argv
const filePath = argv[2]

fs.readFile(filePath, "utf-8", (err, data) => {
  if (err) {
    console.error(err)
    return
  }
  else {
    console.log(data)
  }
})
