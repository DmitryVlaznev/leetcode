// Given a 2d grid map of '1's (land) and '0's (water), count the number
// of islands. An island is surrounded by water and is formed by
// connecting adjacent lands horizontally or vertically. You may assume
// all four edges of the grid are all surrounded by water.

// Example 1:

// Input:
// 11110
// 11010
// 11000
// 00000

// Output: 1
// Example 2:

// Input:
// 11000
// 11000
// 00100
// 00011

// Output: 3


// This solution isn't optimal, it is a trial of union-find algorithm
// using.

class UnionFindCompressed {
    /**
     * Create a parents data array.
     * @param {number} n
     */
    constructor(n) {
        this.parents = new Array(n);
        for (let i = 0; i < n; i++) {
            this.parents[i] = i;
        }
    }

    /**
     * Find a node root.
     * @param {number} index
     */
    root(index) {
        while (this.parents[index] !== index) {
            this.parents[index] = this.parents[this.parents[index]];
            index = this.parents[index];
        }
        return index;
    }

    /**
     * Are the nodes connected?
     *
     * @param {number} a
     * @param {number} b
     *
     * @returns {boolean} Check result.
     */
    connected(a, b) {
        return this.root(a) === this.root(b);
    }

    /**
     * Connect two nodes.
     *
     * @param {number} a
     * @param {number} b
     */
    union(a, b) {
        const ra = this.root(a);
        const rb = this.root(b);
        this.parents[ra] = rb;
    }
}

/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    const rows = grid.length;
    if (rows === 0) {
        return 0;
    }
    const cols = grid[0].length;

    const uf = new UnionFindCompressed(rows * cols);
    toFlatIndex = (row, col) => row * cols + col;
    const land = new Set();

    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            if (grid[row][col] === '0') {
                continue;
            }
            const currentIndex = toFlatIndex(row, col);
            land.add(currentIndex);

            // Check vertical connectivity.
            if (row > 0 && grid[row - 1][col] === '1') {
                uf.union(currentIndex, toFlatIndex(row - 1, col));
            }
            if (row < rows - 1 && grid[row + 1][col] === '1') {
                uf.union(currentIndex, toFlatIndex(row + 1, col));
            }

            // Check horizontal connectivity.
            if (col > 0 && grid[row][col - 1] === '1') {
                uf.union(currentIndex, toFlatIndex(row, col - 1));
            }
            if (col < cols - 1 && grid[row][col + 1] === '1') {
                uf.union(currentIndex, toFlatIndex(row, col + 1));
            }
        }
    }

    const roots = new Set();
    for (let item of land) {
        roots.add(uf.root(item));
    }
    return roots.size;
};

const t1 = ["11110", "11010", "11000", "00000"];
console.log("1 = ", numIslands(t1));

const t2 = ["11000", "11000", "00100", "00011"];
console.log("3 = ", numIslands(t2));

const t3 = [];
console.log("0 = ", numIslands(t3));

const t4 = ["1"];
console.log("1 = ", numIslands(t4));

const t5 = ["0"];
console.log("0 = ", numIslands(t5));

const t6 = [["1","0","1","1","0","1","1"]];
console.log("3 = ", numIslands(t6));

const t7 = [["1"],["0"],["1"],["1"],["0"],["1"],["1"]];
console.log("3 = ", numIslands(t7));