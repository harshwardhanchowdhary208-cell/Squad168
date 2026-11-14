/*
Challenge #4

Given the array nums consisting of 2N elements in the form [x1, x2, ..., xn, y1, y2, ..., yn].
Return the array in the form [x1, y1, x2, y2, ..., xn, yn].

Input Format:
The first line of input contains the size of an array 2N
The second line has the elements of an array
The third line has the value of N

Output Format:
The output consists of the array in the form [x1, y1, x2, y2, ..., xn, yn]

Example 1:
Input:
6
2 5 1 3 4 7
3

Output:
2 3 5 4 1 7
*/

const fs = require('fs');

function shuffleArray() {
  const input = fs.readFileSync(0, 'utf-8').trim().split('\n');
  if (input.length < 3) return;

  const size = parseInt(input[0].trim(), 10);
  const nums = input[1].trim().split(/\s+/).map(Number);
  const n = parseInt(input[2].trim(), 10);

  const result = [];
  for (let i = 0; i < n; i++) {
    result.push(nums[i]);
    result.push(nums[i + n]);
  }

  console.log(result.join(' '));
}

shuffleArray();
