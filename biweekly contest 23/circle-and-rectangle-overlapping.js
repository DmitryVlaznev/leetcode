// 5361. Circle and Rectangle Overlapping

// Given a circle represented as (radius, x_center, y_center) and an
// axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1,
// y1) are the coordinates of the bottom-left corner, and (x2, y2) are
// the coordinates of the top-right corner of the rectangle.

// Return True if the circle and rectangle are overlapped otherwise
// return False.

// In other words, check if there are any point (xi, yi) such that
// belongs to the circle and the rectangle at the same time.


// Example 1:
// Input: radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
// Output: true
// Explanation: Circle and rectangle share the point (1,0)

// Example 2:
// Input: radius = 1, x_center = 0, y_center = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
// Output: true

// Example 3:
// Input: radius = 1, x_center = 1, y_center = 1, x1 = -3, y1 = -3, x2 = 3, y2 = 3
// Output: true
// Example 4:

// Input: radius = 1, x_center = 1, y_center = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
// Output: false

/**
 * @param {number} radius
 * @param {number} x_center
 * @param {number} y_center
 * @param {number} x1
 * @param {number} y1
 * @param {number} x2
 * @param {number} y2
 * @return {boolean}
 */
var checkOverlap = function(radius, x_center, y_center, x1, y1, x2, y2) {
    if (x_center >= x1 && x_center <= x2 && y_center >= y1 && y_center <= y2) {
        return true;
    }

    const d = (xa, ya, xb, yb) => {
        const dx = xa - xb;
        const dy = ya - yb;
        return Math.sqrt(dx**2 + dy**2);
    };

    if (Math.abs(x_center - x1) <= radius) {
        if (y_center >= Math.min(y1, y2) && y_center <= Math.max(y1, y2)) {
            return true;
        }
        if (d(x_center, y_center, x1, y1) < radius || d(x_center, y_center, x1, y2) < radius) {
            return true;
        }
    }
    if (Math.abs(x_center - x2) <= radius) {
        if (y_center >= Math.min(y1, y2) && y_center <= Math.max(y1, y2)) {
            return true;
        }
        if (d(x_center, y_center, x2, y1) < radius || d(x_center, y_center, x2, y2) < radius) {
            return true;
        }
    }
    if (Math.abs(y_center - y1) <= radius) {
        if (x_center >= Math.min(x1, x2) && x_center <= Math.max(x1, x2)) {
            return true;
        }
        if (d(x_center, y_center, x1, y1) < radius || d(x_center, y_center, x2, y1) < radius) {
            return true;
        }
    }
    if (Math.abs(y_center - y2) <= radius) {
        if (x_center >= Math.min(x1, x2) && x_center <= Math.max(x1, x2)) {
            return true;
        }
        if (d(x_center, y_center, x1, y2) < radius || d(x_center, y_center, x2, y2) < radius) {
            return true;
        }
    }
    return false;
};

console.log("true", checkOverlap(1, 0, 0, 1, -1, 3, 1));
console.log("true", checkOverlap(1, 0, 0, -1, 0, 0, 1));
console.log("true", checkOverlap(1, 1, 1, -3, -3, 3, 3));
console.log("false", checkOverlap(1, 1, 1, 1, -3, 2, -1));
console.log("true", checkOverlap(1, 0, 0, 1, -1, 3, 1));

// Nice python solution
// [max(x1,min(xc,x2)), max(y1,min(yc,y2))] - the nearest point
//
// def checkOverlap(self, r, xc, yc, x1, y1, x2, y2):
//     a = (xc-max(x1,min(xc,x2)))**2
//     b = (yc-max(y1,min(yc,y2)))**2
//     return r*r >= a + b
