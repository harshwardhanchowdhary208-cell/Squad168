/*
Challenge #11

Given an array of N integers, print the elements alternately 
from the start and the end of the array until the pointers cross.

Start by printing the first element, then the last element, 
then the second element, then the second last element, and so on.

If there is a middle element left when N is odd, print it only once.

Input:
- The first line contains an integer N representing the number of elements in the array.
- The second line contains N space-separated integers.

Output:
- Print the elements alternately from the start and end, separated by a space.
*/

const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

let index = 0;
let n = input[index++];
let arr = [];

for (let i = 0; i < n; i++) {
    arr.push(input[index++]);
}

let left = 0;
let right = n - 1;
let result = [];

// Use a two-pointer approach to collect elements alternately
while (left <= right) {
    if (left === right) {
        // If pointers meet at the middle element, add it once
        result.push(arr[left]);
    } else {
        // Otherwise, add the element from the start and then from the end
        result.push(arr[left]);
        result.push(arr[right]);
    }
    left++;
    right--;
}

// Print the output space-separated
console.log(result.join(" "));
