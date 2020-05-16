// 1446. Consecutive Characters

// Given a string s, the power of the string is the maximum length of a
// non-empty substring that contains only one unique character.

// Return the power of the string.

// Example 1:
// Input: s = "leetcode"
// Output: 2
// Explanation: The substring "ee" is of length 2 with the character 'e' only.

// Example 2:
// Input: s = "abbcccddddeeeeedcba"
// Output: 5
// Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

// Example 3:
// Input: s = "triplepillooooow"
// Output: 5

// Example 4:
// Input: s = "hooraaaaaaaaaaay"
// Output: 11

// Example 5:
// Input: s = "tourist"
// Output: 1

// Constraints:
// 1 <= s.length <= 500
// s contains only lowercase English letters.

/**
 * @param {string} s
 * @return {number}
 */
var maxPower = function(s) {
    let mp = 0;
    let p = 0;
    for (let i = 0; i < s.length; i++) {
        if (i == 0 || s[i] != s[i - 1]) {
            p = 1;
        } else {
            p++;
        }
        mp = Math.max(mp, p);
    }
    return mp;
};

console.log("2 = ", maxPower("leetcode"));
console.log("5 = ", maxPower("abbcccddddeeeeedcba"));
console.log("5 = ", maxPower("triplepillooooow"));
console.log("11 = ", maxPower("hooraaaaaaaaaaay"));
console.log("1 = ", maxPower("tourist"));
console.log("3 = ", maxPower("tttourist"));
console.log("4 = ", maxPower("touristttt"));
console.log("0 = ", maxPower(""));
