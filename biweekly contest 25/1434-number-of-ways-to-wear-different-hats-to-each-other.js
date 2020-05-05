// 5387. Number of Ways to Wear Different Hats to Each Other

// Difficulty:Hard
// There are n people and 40 types of hats labeled from 1 to 40.

// Given a list of list of integers hats, where hats[i] is a list of all hats preferred by the i-th person.

// Return the number of ways that the n people wear different hats to each other.

// Since the answer may be too large, return it modulo 10^9 + 7.

// Example 1:
// Input: hats = [[3,4],[4,5],[5]]
// Output: 1
// Explanation: There is only one way to choose hats given the conditions.
// First person choose hat 3, Second person choose hat 4 and last one hat 5.

// Example 2:
// Input: hats = [[3,5,1],[3,5]]
// Output: 4
// Explanation: There are 4 ways to choose hats
// (3,5), (5,3), (1,3) and (1,5)

// Example 3:
// Input: hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
// Output: 24
// Explanation: Each person can choose hats labeled from 1 to 4.
// Number of Permutations of (1,2,3,4) = 24.

// Example 4:

// Input: hats = [[1,2,3],[2,3,5,6],[1,3,7,9],[1,8,9],[2,5,7]]
// Output: 111

// Constraints:
// n == hats.length
// 1 <= n <= 10
// 1 <= hats[i].length <= 40
// 1 <= hats[i][j] <= 40
// hats[i] contains a list of unique integers.


/**
 * @param {number[][]} hats
 * @return {number}
 */
var numberWays = function(hats) {
    const people = hats.length;
    const preferred = new Array(41);
    for (let i = 0; i < 41; i++) {preferred[i] = 0};
    for (let i = 0; i < people; i++) {
        for (let j = 0; j < hats[i].length; j++) {
            preferred[hats[i][j]] = 1;
        }
    }
    let ways = 0;
    check(0, preferred);
    return ways;

    function check(person, rest) {
        if (person == people - 1) {
            for (let i = 0; i < hats[person].length; i++) {
                if (rest[hats[person][i]]) {
                    ways = (ways + 1) % 1000000007;
                }
            }
            return;
        }

        for (let i = 0; i < hats[person].length; i++) {
            if (rest[hats[person][i]]) {
                rest[hats[person][i]] = 0;
                check(person + 1, rest);
                rest[hats[person][i]] = 1;
            }
        }
    }
};

// console.log("1 = ", numberWays([[3,4],[4,5],[5]]));
// console.log("4 = ", numberWays([[3,5,1],[3,5]]));
// console.log("24 = ", numberWays([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]));
console.log("111 = ", numberWays([[1,2,3],[2,3,5,6],[1,3,7,9],[1,8,9],[2,5,7]]));

