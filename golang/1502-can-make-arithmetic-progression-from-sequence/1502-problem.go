// 1502. Can Make Arithmetic Progression From Sequence

// Easy

// A sequence of numbers is called an arithmetic progression if the
// difference between any two consecutive elements is the same.

// Given an array of numbers arr, return true if the array can be
// rearranged to form an arithmetic progression. Otherwise, return
// false.

// Example 1:
// Input: arr = [3,5,1]
// Output: true

// Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with
// differences 2 and -2 respectively, between each consecutive elements.

// Example 2:
// Input: arr = [1,2,4]
// Output: false

// Explanation: There is no way to reorder the elements to obtain an
// arithmetic progression.

// Constraints:

// 2 <= arr.length <= 1000
// -10^6 <= arr[i] <= 10^6

package main

import (
	"fmt"
	"sort"
	"utils/checkers"
)

func canMakeArithmeticProgression(arr []int) bool {
	sort.Ints(arr)
	step := arr[1] - arr[0]
	for i := 2; i < len(arr); i++ {
		if arr[i]-arr[i-1] != step {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println("..-== [1502. Can Make Arithmetic Progression From Sequence] ==-..")

	fmt.Println(checkers.CheckScalar(true, canMakeArithmeticProgression([]int{3, 5, 1})))
	fmt.Println(checkers.CheckScalar(true, canMakeArithmeticProgression([]int{-3, -5, -1})))
	fmt.Println(checkers.CheckScalar(false, canMakeArithmeticProgression([]int{1, 2, 4})))
	fmt.Println(checkers.CheckScalar(true, canMakeArithmeticProgression([]int{1, 2})))
	fmt.Println(checkers.CheckScalar(true, canMakeArithmeticProgression([]int{0, -10, 5, -5})))
}
