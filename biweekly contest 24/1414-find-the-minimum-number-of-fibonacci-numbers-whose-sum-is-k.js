// 5373. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
// User Accepted:73
// User Tried:92
// Total Accepted:73
// Total Submissions:98
// Difficulty:Medium

// Given the number k, return the minimum number of Fibonacci numbers
// whose sum is equal to k, whether a Fibonacci number could be used
// multiple times.

// The Fibonacci numbers are defined as:

// F1 = 1
// F2 = 1
// Fn = Fn-1 + Fn-2 , for n > 2.

// It is guaranteed that for the given constraints we can always find
// such fibonacci numbers that sum k.

// Example 1:
// Input: k = 7
// Output: 2
// Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ...
// For k = 7 we can use 2 + 5 = 7.

// Example 2:
// Input: k = 10
// Output: 2
// Explanation: For k = 10 we can use 2 + 8 = 10.

// Example 3:
// Input: k = 19
// Output: 3
// Explanation: For k = 19 we can use 1 + 5 + 13 = 19.

/**
 * @param {number} k
 * @return {number}
 */
var findMinFibonacciNumbers = function(k) {
    if (k < 3) return 1;

    const nums = [1, 1];
    let cur = 2;
    while (cur <= k) {
        nums.push(cur);
        cur = cur + nums[nums.length - 2];
    }

    p = nums.length - 1;
    sum = nums[p]
    p--;
    count = 1
    while (sum !== k && p >= 0) {
        if (sum + nums[p] <= k) {
            sum += nums[p];
            count++;
        }
        p--;
    }
    return count;
};

console.log("3 = ", findMinFibonacciNumbers(19));
console.log("2 = ", findMinFibonacciNumbers(7));
console.log("2 = ", findMinFibonacciNumbers(10));
console.log("3 = ", findMinFibonacciNumbers(100));
console.log("1 = ", findMinFibonacciNumbers(1));
console.log("1 = ", findMinFibonacciNumbers(2));
