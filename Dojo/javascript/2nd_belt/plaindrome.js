/*
Challenge #4
Write a program to determine if a given integer is a palindrome number or not. 
A palindrome number is a number that remains the same when its digits are reversed. 
If N is a palindrome number, print True and otherwise print False.

Input Format:
A single line of input consists of the integer N

Output Format:
A single line of output of True/False
*/

const fs = require('fs');

// Read input from standard input
const input = fs.readFileSync(0, 'utf-8').trim();

if (input.length > 0) {
    // Reverse the string representation of the number
    const reversed = input.split('').reverse().join('');
    
    // Check if the original string matches the reversed string
    if (input === reversed) {
        console.log("True");
    } else {
        console.log("False");
    }
}
