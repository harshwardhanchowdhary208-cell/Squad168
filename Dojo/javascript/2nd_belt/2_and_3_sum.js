/*
Challenge #2
A frog is trying to reach exactly the Nth step. The frog can jump either 2 steps or 3 steps at a time.
Determine whether the frog can reach exactly the Nth step using any combination of jumps of size 2 and 3.
Print "Yes" if it is possible, otherwise print "No".

Input:
- A single integer N representing the step number.

Output:
- Print "Yes" if the frog can reach exactly step N.
- Otherwise, print "No".
*/

const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim();

if (input !== "") {
  const n = Number(input);

  if (n >= 2 || n === 0) {
    console.log("Yes");
  } else {
    console.log("No");
  }
}
