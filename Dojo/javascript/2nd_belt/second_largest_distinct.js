/*
Challenge #13
Given a list of integers, find the second largest distinct number in the list.
If there is no second largest distinct number, print -1.
*/

const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split(/\s+/);

let index = 0;
const n = parseInt(input[index++]);
let arr = [];

for (let i = 0; i < n; i++) {
    arr.push(Number(input[index++]));
}

// Remove duplicates and sort the unique numbers in descending order
const uniqueArr = [...new Set(arr)].sort((a, b) => b - a);

// Output the second largest element if it exists, otherwise print -1
if (uniqueArr.length >= 2) {
    console.log(uniqueArr[1]);
} else {
    console.log(-1);
}
