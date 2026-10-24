const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split(/\s+/);

let idx = 0;
const T = parseInt(input[idx++]);

for (let tc = 0; tc < T; tc++) {
    const N = parseInt(input[idx++]);
    const A = parseInt(input[idx++]);
    const B = parseInt(input[idx++]);
    
    let profit = [];
    for (let i = 0; i < N; i++) {
        profit.push(parseInt(input[idx++]));
    }
    
    // // Write your logic here
    // Compute prefix sums: pref[i] represents the sum of the first i elements
    let pref = new Array(N + 1);
    pref[0] = 0;
    for (let i = 0; i < N; i++) {
        pref[i + 1] = pref[i] + profit[i];
    }

    let max_sum = -Infinity;
    let deque = []; 
    let head = 0; // Pointer to the front of the deque for O(1) removals

    for (let i = A; i <= N; i++) {
        // A new valid starting index candidate enters the window: j = i - A
        let new_j = i - A;
        
        // Maintain a monotonically increasing deque (front element will always be the minimum)
        while (deque.length > head && pref[deque[deque.length - 1]] >= pref[new_j]) {
            deque.pop();
        }
        deque.push(new_j);
        
        // Remove indices from the front that fall out of the valid range [i - B, i - A]
        while (deque.length > head && deque[head] < i - B) {
            head++;
        }
        
        // The maximum sum ending at index i-1 with a length between A and B
        let current_max = pref[i] - pref[deque[head]];
        if (current_max > max_sum) {
            max_sum = current_max;
        }
    }
    
    console.log(max_sum);
}
