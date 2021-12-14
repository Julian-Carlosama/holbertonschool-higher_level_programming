#!/usr/bin/node
const intg = parseInt(process.argv[2]);
if (!intg) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < intg; i++) {
    console.log('C is fun');
  }
}
