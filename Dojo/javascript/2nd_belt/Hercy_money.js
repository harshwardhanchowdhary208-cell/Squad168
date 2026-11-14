/*
Challenge #3

Hercy wants to save money for his first car. He puts money in the bank every day following this pattern:
- On the first Monday, he puts in 1
- From Tuesday to Sunday, he puts in 1 more than the previous day
- On every new Monday, he puts in 1 more than the previous Monday

Given an integer n, representing the number of days, find the total amount of money saved after the nth day.

Input Format:
The first line contains an integer n, the number of days.

Output Format:
Print a single integer, the total amount of money saved after n days.
*/

const fs = require("fs");
const n = Number(fs.readFileSync(0, "utf8").trim());

// Write your logic here
function totalMoney(n) {
  const weeks = Math.floor(n / 7);
  const remainingDays = n % 7;

  // Sum of full weeks:
  // Week 1 = 28 (1+2+3+4+5+6+7), Week 2 = 35, Week k = 28 + 7*(k-1)
  const fullWeeksSum = (weeks * (2 * 28 + (weeks - 1) * 7)) / 2;

  // Sum of remaining days in the last incomplete week:
  // Starts at (weeks + 1) on Monday and increases by 1 each day
  const startDayAmount = weeks + 1;
  const remainingSum =
    (remainingDays * (2 * startDayAmount + (remainingDays - 1))) / 2;

  return fullWeeksSum + remainingSum;
}

console.log(totalMoney(n));
