// 1492. The kth Factor of n

// Given two positive integers n and k.
// A factor of an integer n is defined as an integer i where n % i == 0.

// Consider a list of all factors of n sorted in ascending order, return
// the kth factor in this list or return -1 if n has less than k
// factors.



// Example 1:
// Input: n = 12, k = 3
// Output: 3
// Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.

// Example 2:
// Input: n = 7, k = 2
// Output: 7
// Explanation: Factors list is [1, 7], the 2nd factor is 7.

// Example 3:
// Input: n = 4, k = 4
// Output: -1
// Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.

// Example 4:
// Input: n = 1, k = 1
// Output: 1
// Explanation: Factors list is [1], the 1st factor is 1.

// Example 5:
// Input: n = 1000, k = 3
// Output: 4
// Explanation: Factors list is [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000].

// Constraints:
// 1 <= k <= n <= 1000

/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var kthFactor = function(n, k) {
    i = 1;
    count = 0;
    while (i <= n) {
        if (n % i == 0) {
            count++;
        }
        if (count == k) {
            return i;
        }
        i++;
    }
    return -1;
};

console.log("3 = ", kthFactor(12, 3));
console.log("7 = ", kthFactor(7, 2));
console.log("-1 = ", kthFactor(4, 4));
console.log("4 = ", kthFactor(1000, 3));