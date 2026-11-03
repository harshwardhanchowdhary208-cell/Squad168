/*
Challenge #14

Write a program to print the multiplication table for a given number N.

Input Format:
The input consists of a single integer N, where 1 <= N <= 30.

Output Format:
Print the multiplication table of N from 1 to 10.
*/

const fs = require('fs');

function main() {
    // Read input from standard input
    const input = fs.readFileSync(0, 'utf-8').trim();
    if (!input) return;
    
    const N = parseInt(input, 10);
    
    // Generate and print the multiplication table from 1 to 10
    for (let i = 1; i <= 10; i++) {
        console.log(`${N} x ${i} = ${N * i}`);
    }
}

main();
