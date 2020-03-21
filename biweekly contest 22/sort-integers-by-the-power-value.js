/**
 * @param {number} lo
 * @param {number} hi
 * @param {number} k
 * @return {number}
 */
var getKth = function(lo, hi, k) {
    const powers = {};
    getPower = (x) => {
        if (x == 1) {
            return 0;
        }
        if (powers[x] != undefined) {
            return powers[x];
        }

        let nextX;
        if (x % 2) {
            nextX = 3 * x + 1;
        } else {
            nextX = x / 2;
        }
        power = 1 + getPower(nextX);
        powers[x] = power;
        return power;
    }

    res = [];
    for(let i = lo; i <= hi; i++) {
        res.push([i, getPower(i)]);
    }
    res.sort((a, b) => {
        if (a[1] < b[1]) return -1;
        if (a[1] > b[1]) return 1;
        return a[0] < b[0] ? -1 : 1;
    });

    return res[k - 1][0];
};

console.log("13 => ", getKth(12, 15, 2));
