/*
Challenge #5
Write a program to calculate and print the Least Common Multiple (LCM) of two numbers. 
Note that if either number is zero, then the LCM of the two numbers is also zero.

Input Format:
The input consists of two integers A and B.

Output Format:
The output consists of LCM of the two numbers.

Example 1:
Input:
4 6
Output:
12
*/

const fs = require('fs');

// Read input from standard input
const input = fs.readFileSync(0, 'utf-8').trim().split(/\s+/);
const a = parseInt(input[0], 10);
const b = parseInt(input[1], 10);

// Function to find Greatest Common Divisor (GCD)
function findGCD(x, y) {
    while (y !== 0) {
        let temp = y;
        y = x % y;
        x = temp;
    }
    return x;
}

// Calculate and print LCM
if (a === 0 || b === 0) {
    console.log(0);
} else {
    const gcd = findGCD(Math.abs(a), Math.abs(b));
    const lcm = Math.abs(a * b) / gcd;
    console.log(lcm);
}
