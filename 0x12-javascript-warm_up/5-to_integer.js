#!/usr/bin/node
const intg = parseInt(process.argv[2]);
if (intg) {
  console.log('My number: ' + intg);
} else {
  console.log('Not a number');
}
