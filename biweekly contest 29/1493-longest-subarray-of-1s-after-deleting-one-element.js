// 1493. Longest Subarray of 1's After Deleting One Element

// Given a binary array nums, you should delete one element from it.

// Return the size of the longest non-empty subarray containing only 1's
// in the resulting array.

// Return 0 if there is no such subarray.

// Example 1:
// Input: nums = [1,1,0,1]
// Output: 3
// Explanation: After deleting the number in position 2, [1,1,1]
// contains 3 numbers with value of 1's.

// Example 2:
// Input: nums = [0,1,1,1,0,1,1,0,1]
// Output: 5
// Explanation: After deleting the number in position 4,
// [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

// Example 3:
// Input: nums = [1,1,1]
// Output: 2
// Explanation: You must delete one element.

// Example 4:
// Input: nums = [1,1,0,0,1,1,1,0,1]
// Output: 4

// Example 5:
// Input: nums = [0,0,0]
// Output: 0

// Constraints:
// 1 <= nums.length <= 10^5
// nums[i] is either 0 or 1.

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function(nums) {
    let last_zero_idx = -1
    let max_seq = 0
    let seq_start = -1
    for (i = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            if (seq_start == -1) {
                seq_start = i;
            }

            let cur = i - seq_start + 1;
            if (last_zero_idx >= seq_start) {
                cur--;
            }
            max_seq = Math.max(max_seq, cur);
        } else {
            if (seq_start == -1) {
                continue;
            }
            if (last_zero_idx < seq_start) {
                last_zero_idx = i;
            } else {
                if (nums[last_zero_idx + 1] == 1) {
                    seq_start = last_zero_idx + 1;
                    last_zero_idx = i;
                } else {
                    last_zero_idx = -1
                    seq_start = -1
                }
            }
        }
    }

    if (max_seq == 0) return 0;
    if (max_seq == nums.length) return max_seq - 1;
    return max_seq;
};

console.log("3 = ", longestSubarray([1,1,0,1]));
console.log("5 = ", longestSubarray([0,1,1,1,0,1,1,0,1]));
console.log("2 = ", longestSubarray([1,1,1]));
console.log("4 = ", longestSubarray([1,1,0,0,1,1,1,0,1]));
console.log("0 = ", longestSubarray([0,0,0]));
console.log("3 = ", longestSubarray([0,0,0,1,1,1,0,0,0,1,0,1,0,1]));
console.log("2 = ", longestSubarray([1,1,0,0,1,0,1,0,0,1]));
