// 1091. Shortest Path in Binary Matrix

// Medium

// Given an n x n binary matrix grid, return the length of the shortest
// clear path in the matrix. If there is no clear path, return -1.

// A clear path in a binary matrix is a path from the top-left cell
// (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such
// that:

// All the visited cells of the path are 0.
// All the adjacent cells of the path are 8-directionally connected
// (i.e., they are different and they share an edge or a corner).
// The length of a clear path is the number of visited cells of this
// path.

// Example 1:
// Input: grid = [[0,1],[1,0]]
// Output: 2

// Example 2:
// Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
// Output: 4

// Example 3:
// Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
// Output: -1

// Constraints:
// n == grid.length
// n == grid[i].length
// 1 <= n <= 100
// grid[i][j] is 0 or 1

package main

import (
	"fmt"
)

type Point struct {
	x int
	y int
}

func get(m *[][]int, r int, c int) int {
	rows, cols := len(*m), len((*m)[0])
	if r < 0 || c < 0 || r >= rows || c >= cols {
		return 1
	}
	return (*m)[r][c]
}

func shortestPathBinaryMatrix(grid [][]int) int {
	rows, cols := len(grid), len(grid[0])

	if grid[0][0] != 0 || grid[rows-1][cols-1] != 0 {
		return -1
	}

	paths := make([][]int, rows)
	for i := 0; i < rows; i++ {
		paths[i] = make([]int, cols)
	}
	paths[0][0] = 1

	deltas := []Point{{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}}
	q := []Point{{0, 0}}

	for len(q) > 0 {
		l, i, nq := len(q), 0, []Point{}
		for i < l {
			p := q[i]
			for _, d := range deltas {
				if get(&grid, p.x+d.x, p.y+d.y) == 0 && get(&paths, p.x+d.x, p.y+d.y) == 0 {
					paths[p.x+d.x][p.y+d.y] = paths[p.x][p.y] + 1
					nq = append(nq, Point{p.x + d.x, p.y + d.y})
				}
			}
			i++
		}
		q = nq
	}
	if paths[rows-1][cols-1] == 0 {
		return -1
	}

	return paths[rows-1][cols-1]
}

func main() {
	fmt.Println("..-== [1091. Shortest Path in Binary Matrix] ==-..")

	grid := [][]int{{0, 0, 0}, {1, 1, 0}, {1, 1, 0}}
	res := shortestPathBinaryMatrix(grid)
	fmt.Println("4 =", res)

	grid = [][]int{{0}}
	res = shortestPathBinaryMatrix(grid)
	fmt.Println("1 =", res)

	grid = [][]int{{1}}
	res = shortestPathBinaryMatrix(grid)
	fmt.Println("-1 =", res)

	grid = [][]int{
		{0, 1, 1, 0, 0, 0},
		{0, 1, 0, 1, 1, 0},
		{0, 1, 1, 0, 1, 0},
		{0, 0, 0, 1, 1, 0},
		{1, 1, 1, 1, 1, 0},
		{1, 1, 1, 1, 1, 0},
	}
	res = shortestPathBinaryMatrix(grid)
	fmt.Println("14 =", res)
}
