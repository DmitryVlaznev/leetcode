// 1432. Max Difference You Can Get From Changing an Integer

// Difficulty:Medium
// You are given an integer num. You will apply the following steps exactly two times:

// Pick a digit x (0 <= x <= 9).
// Pick another digit y (0 <= y <= 9). The digit y can be equal to x.
// Replace all the occurrences of x in the decimal representation of num by y.
// The new integer cannot have any leading zeros, also the new integer cannot be 0.
// Let a and b be the results of applying the operations to num the first and second times, respectively.

// Return the max difference between a and b.

// Example 1:
// Input: num = 555
// Output: 888
// Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
// The second time pick x = 5 and y = 1 and store the new integer in b.
// We have now a = 999 and b = 111 and max difference = 888

// Example 2:
// Input: num = 9
// Output: 8
// Explanation: The first time pick x = 9 and y = 9 and store the new integer in a.
// The second time pick x = 9 and y = 1 and store the new integer in b.
// We have now a = 9 and b = 1 and max difference = 8

// Example 3:
// Input: num = 123456
// Output: 820000

// Example 4:
// Input: num = 10000
// Output: 80000

// Example 5:
// Input: num = 9288
// Output: 8700

// Constraints:
// 1 <= num <= 10^8

/**
 * @param {number} num
 * @return {number}
 */
var maxDiff = function(num) {
    const arr = num.toString().split("").map(v => parseInt(v, 10))
    l = arr.length
    let min = arr.slice()
    let max = arr.slice();

    // Find minimum
    let p = 0;
    let replace, replace_to;
    if (min[0] == 1) {
        replace = null
        replace_to = 0
    } else {
        replace = min[0]
        replace_to = 1
    }
    while(p < l) {
        if (replace === null && min[p] !== 1 && min[p] !== 0) {
            replace = min[p]
            min[p] = 0
        } else if(replace !== null && min[p] === replace) {
            min[p] = replace_to
        }
        p++;
    }
    min = parseInt(min.join(""))

    // Find maximum
    p = 0;
    replace = null
    replace_to = 9
    while(p < l) {
        if (replace === null && max[p] !== 9) {
            replace = max[p]
            max[p] = replace_to
        } else if(replace !== null && max[p] === replace) {
            max[p] = replace_to
        }
        p++;
    }
    max = parseInt(max.join(""))
    return max - min;
};

console.log("888 = ", maxDiff(555));
console.log("8 = ", maxDiff(9));
console.log("820000 = ", maxDiff(123456));
console.log("80000 = ", maxDiff(10000));
console.log("8700 = ", maxDiff(9288));

// console.log("num =", num, "min =", min);
// console.log("num =", num, "max =", max);

// maxDiff(123425)
// maxDiff(10001)
// maxDiff(90009)
// maxDiff(10005)
// maxDiff(90005)
// maxDiff(12200345)
// maxDiff(999991200345)





// const arr = [];
    // let factor = 10
    // let digit;
    // while (num > 0) {
    //     digit = num % factor
    //     arr.push(digit);
    //     num -= digit * factor / 10;
    //     factor *= 10
    // }
    // arr.reverse();