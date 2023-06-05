// 1232. Check If It Is a Straight Line

// Easy

// You are given an array coordinates, coordinates[i] = [x, y], where
// [x, y] represents the coordinate of a point. Check if these points
// make a straight line in the XY plane.

// Example 1:
// Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
// Output: true

// Example 2:
// Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
// Output: false

// Constraints:
// 2 <= coordinates.length <= 1000
// coordinates[i].length == 2
// -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
// coordinates contains no duplicate point.

package main

import (
	"fmt"
	"utils/checkers"
)

func checkStraightLine(coordinates [][]int) bool {
	if len(coordinates) < 3 {
		return true
	}
	x1, y1, x2, y2 := coordinates[0][0], coordinates[0][1], coordinates[1][0], coordinates[1][1]
	for _, p := range coordinates[2:] {
		if (p[0]-x1)*(y2-y1) != (p[1]-y1)*(x2-x1) {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println("..-== [1232. Check If It Is a Straight Line] ==-..")

	fmt.Println(checkers.CheckScalar(true, checkStraightLine([][]int{{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}})))
	fmt.Println(checkers.CheckScalar(false, checkStraightLine([][]int{{1, 1}, {2, 2}, {3, 4}, {4, 5}, {5, 6}, {7, 7}})))
	fmt.Println(checkers.CheckScalar(true, checkStraightLine([][]int{{0, 0}, {0, 1}, {0, -1}})))
}
