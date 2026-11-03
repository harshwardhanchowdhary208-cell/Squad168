/*
Challenge #10
Given a list of integers, find the range of the list.
The range is defined as: Range = Largest element - Smallest element
Print the range of the given list.

Input Format:
- The first line contains an integer N, the number of elements in the list.
- The second line contains N space-separated integers.

Output Format:
- Print a single integer representing the range of the numbers in the list.
*/

const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split(/\s+/);

let index = 0;
const n = Number(input[index++]);
let arr = [];

for (let i = 0; i < n; i++) {
    arr.push(Number(input[index++]));
}

// Write your logic here
if (n > 0) {
    let minVal = arr[0];
    let maxVal = arr[0];

    for (let i = 1; i < n; i++) {
        if (arr[i] < minVal) minVal = arr[i];
        if (arr[i] > maxVal) maxVal = arr[i];
    }

    const range = maxVal - minVal;
    console.log(range);
} else {
    console.log(0);
}
