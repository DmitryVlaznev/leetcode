// 5360. Count Largest Group

// Given an integer n. Each number from 1 to n is grouped according to the sum of its digits.

// Return how many groups have the largest size.

// Example 1:
// Input: n = 13
// Output: 4
// Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
// [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups with largest size.

// Example 2:
// Input: n = 2
// Output: 2
// Explanation: There are 2 groups [1], [2] of size 1.

// Example 3:
// Input: n = 15
// Output: 6

// Example 4:
// Input: n = 24
// Output: 5

/**
 * @param {number} n
 * @return {number}
 */
var countLargestGroup = function(n) {
    const groups = {};
    for (let i = 1; i <=n; i++) {
        const b = (i).toString().split("").reduce((acc, digit) => acc + parseInt(digit, 10), 0);
        if (b in groups) {
            groups[b]++;
        } else {
            groups[b] = 1;
        }
    }
    const items = Object.values(groups);
    items.sort((a, b) => a < b ? 1 : a > b ? -1 : 0);

    let max = 1;
    let i = 1;
    while(items[i] === items[0]) {
        max++;
        i++;
    };

    return max;
};

console.log("4 >> ", countLargestGroup(13));
console.log("2 >> ", countLargestGroup(2));
console.log("6 >> ", countLargestGroup(15));
console.log("5 >> ", countLargestGroup(24));


