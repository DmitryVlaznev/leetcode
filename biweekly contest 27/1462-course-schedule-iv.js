// 1462. Course Schedule IV

// There are a total of n courses you have to take, labeled from 0 to
// n-1.

// Some courses may have direct prerequisites, for example, to take
// course 0 you have first to take course 1, which is expressed as a
// pair: [1,0]

// Given the total number of courses n, a list of direct prerequisite
// pairs and a list of queries pairs.

// You should answer for each queries[i] whether the course
// queries[i][0] is a prerequisite of the course queries[i][1] or not.

// Return a list of boolean, the answers to the given queries.

// Please note that if course a is a prerequisite of course b and course
// b is a prerequisite of course c, then, course a is a prerequisite of
// course c.


// Example 1:
// Input: n = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
// Output: [false,true]
// Explanation: course 0 is not a prerequisite of course 1 but the opposite is true.

// Example 2:
// Input: n = 2, prerequisites = [], queries = [[1,0],[0,1]]
// Output: [false,false]
// Explanation: There are no prerequisites and each course is independent.

// Example 3:
// Input: n = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
// Output: [true,true]

// Example 4:
// Input: n = 3, prerequisites = [[1,0],[2,0]], queries = [[0,1],[2,0]]
// Output: [false,true]

// Example 5:
// Input: n = 5, prerequisites = [[0,1],[1,2],[2,3],[3,4]], queries = [[0,4],[4,0],[1,3],[3,0]]
// Output: [true,false,true,false]

/**
 * @param {number} n
 * @param {number[][]} prerequisites
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var checkIfPrerequisite = function(n, prerequisites, queries) {
    const graph = new Array(n);
    for (let i = 0; i < n; i++) {
        graph[i] = [];
    }
    for (let [c, p] of prerequisites) {
        graph[c].push(p);
    }

    const res = Array.apply(null, new Array(queries.length)).map(() => false);
    let p = 0;
    for ([src, dst] of queries) {
        const stack = [src];
        const seen = new Set([src]);

        while(stack.length) {
            const node = stack.pop();
            if (node === dst) {
                res[p] = true;
                break;
            }
            for (next of graph[node]) {
                if (!seen.has(next)) {
                    stack.push(next);
                    seen.add(next);
                }
            }
        }
        p++;
    }
    return res;
};

console.log("[false,true]", checkIfPrerequisite(2, [[1,0]], [[0,1],[1,0]]));
console.log("[false,false]", checkIfPrerequisite(2, [], [[1,0],[0,1]]));
console.log("[false,false]", checkIfPrerequisite(2, [], [[1,0],[0,1]]));
console.log("[true,false,true,false]", checkIfPrerequisite(5, [[0,1],[1,2],[2,3],[3,4]], [[0,4],[4,0],[1,3],[3,0]]));


