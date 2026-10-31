/*
Challenge #3

A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself. 
In other words, a perfect number is the sum of its positive divisors (excluding itself), and it is not a prime number. 
The smallest perfect number is 6, which is the sum of its divisors 1, 2, and 3.

Write a program to determine whether a given number is a perfect number or not.

Input Format:
The input consists of a single integer N, where 1 <= N <= 10^9.

Output Format:
Print "Perfect" if the input number is a perfect number, otherwise print "Not Perfect".

Example 1:
Input:
6
Output:
Perfect
Explanation:
The divisors of 6 (excluding 6 itself) are 1, 2, 3. Sum of divisors: 1 + 2 + 3 = 6
*/

const fs = require('fs');

function checkPerfectNumber() {
    // Read input from standard input
    const input = fs.readFileSync(0, 'utf-8').trim();
    if (!input) return;
    
    const N = parseInt(input, 10);
    
    // 1 is not a perfect number as its proper divisors sum to 0
    if (N <= 1) {
        console.log("Not Perfect");
        return;
    }
    
    let sum = 1; // 1 is always a proper divisor for any N > 1
    const limit = Math.sqrt(N);
    
    // Find all divisors up to the square root of N
    for (let i = 2; i <= limit; i++) {
        if (N % i === 0) {
            sum += i;
            // If the divisors are distinct, add the matching divisor
            if (i !== N / i) {
                sum += N / i;
            }
        }
    }
    
    // Check if the sum of proper divisors equals the original number
    if (sum === N) {
        console.log("Perfect");
    } else {
        console.log("Not Perfect");
    }
}

checkPerfectNumber();
