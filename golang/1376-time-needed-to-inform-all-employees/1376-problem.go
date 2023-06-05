// 1376. Time Needed to Inform All Employees

// Medium

// A company has n employees with a unique ID for each employee from 0
// to n - 1. The head of the company is the one with headID.

// Each employee has one direct manager given in the manager array where
// manager[i] is the direct manager of the i-th employee,
// manager[headID] = -1. Also, it is guaranteed that the subordination
// relationships have a tree structure.

// The head of the company wants to inform all the company employees of
// an urgent piece of news. He will inform his direct subordinates, and
// they will inform their subordinates, and so on until all employees
// know about the urgent news.

// The i-th employee needs informTime[i] minutes to inform all of his
// direct subordinates (i.e., After informTime[i] minutes, all his
// direct subordinates can start spreading the news).

// Return the number of minutes needed to inform all the employees about
// the urgent news.

// Example 1:
// Input: n = 1, headID = 0, manager = [-1], informTime = [0]
// Output: 0
// Explanation: The head of the company is the only employee in the
// company.

// Example 2:

// Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
// Output: 1
// Explanation: The head of the company with id = 2 is the direct
// manager of all the employees in the company and needs 1 minute to
// inform them all.
// The tree structure of the employees in the company is shown.

// Constraints:
// 1 <= n <= 10^5
// 0 <= headID < n
// manager.length == n
// 0 <= manager[i] < n
// manager[headID] == -1
// informTime.length == n
// 0 <= informTime[i] <= 1000
// informTime[i] == 0 if employee i has no subordinates.
// It is guaranteed that all the employees can be informed.

package main

import (
	"fmt"
	"utils/checkers"
)

func dfs(nodeID int, graph *[][]int, informTime *[]int) int {
	max := 0
	for _, managerID := range (*graph)[nodeID] {
		managerMax := dfs(managerID, graph, informTime)
		if managerMax > max {
			max = managerMax
		}
	}
	return max + (*informTime)[nodeID]
}

func numOfMinutes(n int, headID int, manager []int, informTime []int) int {
	var graph [][]int = make([][]int, n)
	for i, mi := range manager {
		if mi > -1 {
			graph[mi] = append(graph[mi], i)
		}
	}
	return dfs(headID, &graph, &informTime)
}

func main() {
	fmt.Println("..-== [1376. Time Needed to Inform All Employees] ==-..")

	fmt.Println(checkers.CheckScalar(0, numOfMinutes(1, 0, []int{-1}, []int{0})))
	fmt.Println(checkers.CheckScalar(1, numOfMinutes(6, 2, []int{2, 2, -1, 2, 2, 2}, []int{0, 0, 1, 0, 0, 0})))
	fmt.Println(checkers.CheckScalar(11, numOfMinutes(7, 2, []int{2, 2, -1, 2, 2, 3, 4}, []int{0, 0, 1, 10, 5, 0, 0})))
	fmt.Println(checkers.CheckScalar(2560, numOfMinutes(11, 4, []int{5, 9, 6, 10, -1, 8, 9, 1, 9, 3, 4}, []int{0, 213, 0, 253, 686, 170, 975, 0, 261, 309, 337})))
}
