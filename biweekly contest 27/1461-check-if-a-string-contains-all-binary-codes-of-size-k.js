// 1461. Check If a String Contains All Binary Codes of Size K

// Given a binary string s and an integer k.
// Return True if any binary code of length k is a substring of s.
// Otherwise, return False.

// Example 1:
// Input: s = "00110110", k = 2
// Output: true
// Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indicies 0, 1, 3 and 2 respectively.

// Example 2:
// Input: s = "00110", k = 2
// Output: true

// Example 3:
// Input: s = "0110", k = 1
// Output: true
// Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring.

// Example 4:
// Input: s = "0110", k = 2
// Output: false
// Explanation: The binary code "00" is of length 2 and doesn't exist in the array.

// Example 5:
// Input: s = "0000000001011100", k = 4
// Output: false

// Constraints:
// 1 <= s.length <= 5 * 10^5
// s consists of 0's and 1's only.
// 1 <= k <= 20

/**
 * @param {string} s
 * @param {number} k
 * @return {boolean}
 */
var hasAllCodes = function(s, k) {
    const subs = new Set();
    for(let i = 0; i <= s.length - k; i++) {
        subs.add(s.substring(i, i + k));
    }
    return subs.size == Math.pow(2, k);
};

console.log(true, hasAllCodes("00110110", 2));
console.log(true, hasAllCodes("00110", 2));
console.log(true, hasAllCodes("0110", 1));
console.log(false, hasAllCodes("0110", 2));
console.log(false, hasAllCodes("0000000001011100", 4));

