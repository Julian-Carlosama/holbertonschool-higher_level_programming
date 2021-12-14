#!/usr/bin/node
const intg = parseInt(process.argv[2]);
if (!intg) {
  console.log('Missing size');
} else {
  for (let i = 0; i < intg; i++) {
    let sq = '';
    for (let j = 0; j < intg; j++) {
      sq += 'X';
    } console.log(sq);
  }
}
