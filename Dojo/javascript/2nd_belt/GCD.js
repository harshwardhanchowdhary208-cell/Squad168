/*
Challenge #3

Write a program to calculate and print the Greatest Common Divisor (GCD) of two numbers. 
Note that if either number is zero, print the other number.

Input Format:
The input consists of two integers A and B.

Output Format:
Print the GCD of the two numbers.

Example 1:
Input:
6 9
Output:
3
*/

const fs = require('fs');

// Read input from standard input (handles space-separated or newline-separated integers)
const input = fs.readFileSync(0, 'utf-8').trim().split(/\s+/);

if (input.length >= 2) {
    let a = Math.abs(parseInt(input[0], 10));
    let b = Math.abs(parseInt(input[1], 10));

    // Euclidean algorithm to calculate GCD
    function findGCD(x, y) {
        while (y !== 0) {
            let temp = y;
            y = x % y;
            x = temp;
        }
        return x;
    }

    console.log(findGCD(a, b));
}
