/**
 * @param {number} n
 * @param {number[][]} reservedSeats
 * @return {number}
 */
var maxNumberOfFamilies = function(n, reservedSeats) {
    reservedSeats.sort((a, b) => {
        if (a[0] < b[0]) return -1;
        if (a[0] > b[0]) return 1;
        return a[1] < b[1] ? -1 : 1;
    })

    let families = 2 * n;
    const checkRowSeats = (reserved) => {
        let left = true;
        let right = true;
        let middle = true;

        for (let i = 0; i < reserved.length; i++) {
            if ([2, 3, 4, 5].includes(reserved[i])) left = false;
            if ([4, 5, 6, 7].includes(reserved[i])) middle = false;
            if ([6, 7, 8, 9].includes(reserved[i])) right = false;
        }

        if (left && right) {
            return;
        }

        if (left || middle || right) {
            families -=1;
            return;
        }

        families -= 2;
    };

    const reserved = reservedSeats.length;
    let r = 0;
    let row = null;
    let rowSeats = [];
    while(r < reserved) {
        if (row === null) {
            row = reservedSeats[r][0];
            rowSeats = [reservedSeats[r][1]];
        }  else {
            rowSeats.push(reservedSeats[r][1])
        }
        if (r === reserved - 1 || reservedSeats[r + 1][0] !== row) {

            checkRowSeats(rowSeats);
            row = null;
            rowSeats = [];
        }
        r++;
    }
    return families;
};

let n, reservedSeats;
n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]];
console.log("4 => ", maxNumberOfFamilies(n, reservedSeats));

n = 2, reservedSeats = [[2,1],[1,8],[2,6]];
console.log("2 => ", maxNumberOfFamilies(n, reservedSeats));

n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]];
console.log("4 => ", maxNumberOfFamilies(n, reservedSeats));