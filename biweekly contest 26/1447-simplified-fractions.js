// 1447. Simplified Fractions

// Given an integer n, return a list of all simplified fractions between
// 0 and 1 (exclusive) such that the denominator is
// less-than-or-equal-to n. The fractions can be in any order.

// Example 1:
// Input: n = 2
// Output: ["1/2"]
// Explanation: "1/2" is the only unique fraction with a denominator less-than-or-equal-to 2.

// Example 2:
// Input: n = 3
// Output: ["1/2","1/3","2/3"]

// Example 3:
// Input: n = 4
// Output: ["1/2","1/3","1/4","2/3","3/4"]
// Explanation: "2/4" is not a simplified fraction because it can be simplified to "1/2".

// Example 4:
// Input: n = 1
// Output: []

// Constraints:
// 1 <= n <= 100

/**
 * @param {number} n
 * @return {string[]}
 */
var simplifiedFractions = function(n) {
    if(n == 1) return [];

    const added = new Set();
    const res = []
    for (let lo = 2; lo <= n; lo++) {
        for (let hi = 1; hi < lo; hi++) {
            let div = hi / lo;
            if (div < 1 && !added.has(div)) {
                res.push(`${hi}/${lo}`)
                added.add(div);
            }
        }
    }
    return res;
};

console.log(simplifiedFractions(1));
console.log(simplifiedFractions(2));
console.log(simplifiedFractions(3));
console.log(simplifiedFractions(4));
