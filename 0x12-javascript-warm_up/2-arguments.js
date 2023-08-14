#!/usr/bin/node

const process = require('process');
const myArgs = process.argv.length - 2;

if (myArgs > 1) {
  console.log('Arguments found');
} else if (myArgs === 1) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
