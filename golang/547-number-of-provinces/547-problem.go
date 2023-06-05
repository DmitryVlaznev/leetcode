// 547. Number of Provinces

// Medium

// There are n cities. Some of them are connected, while some are not.
// If city a is connected directly with city b, and city b is connected
// directly with city c, then city a is connected indirectly with city
// c.

// A province is a group of directly or indirectly connected cities and
// no other cities outside of the group.

// You are given an n x n matrix isConnected where isConnected[i][j] = 1
// if the ith city and the jth city are directly connected, and
// isConnected[i][j] = 0 otherwise.

// Return the total number of provinces.

// Example 1:
// Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
// Output: 2

// Example 2:
// Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
// Output: 3

// Constraints:
// 1 <= n <= 200
// n == isConnected.length
// n == isConnected[i].length
// isConnected[i][j] is 1 or 0.
// isConnected[i][i] == 1
// isConnected[i][j] == isConnected[j][i]

package main

import (
	"fmt"
	"utils/checkers"
)

func visitNeighbors(city int, isConnected *[][]int, visited *map[int]bool) {
	q := []int{city}
	for len(q) > 0 {
		nq := []int{}
		for _, p := range q {
			(*visited)[p] = true
			for c, connected := range (*isConnected)[p] {
				if !(*visited)[c] && p != c && connected == 1 {
					nq = append(nq, c)
				}
			}
		}
		q = nq
	}
}

func findCircleNum(isConnected [][]int) int {
	n, visited, provinces := len(isConnected), map[int]bool{}, 0
	for i := 0; i < n; i++ {
		if visited[i] {
			continue
		}
		provinces++
		visitNeighbors(i, &isConnected, &visited)
	}
	return provinces
}

func main() {
	fmt.Println("..-== [547. Number of Provinces] ==-..")

	fmt.Println(checkers.CheckScalar(2, findCircleNum([][]int{{1, 1, 0}, {1, 1, 0}, {0, 0, 1}})))
	fmt.Println(checkers.CheckScalar(3, findCircleNum([][]int{{1, 0, 0}, {0, 1, 0}, {0, 0, 1}})))
	fmt.Println(checkers.CheckScalar(1, findCircleNum([][]int{{1}})))
}
