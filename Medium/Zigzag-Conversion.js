/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
 var convert = function(s, numRows) {
    var row = 0;
    var reverse = false;
    var l = [];
    var str = "";
    if (numRows == 1) return s
    for (let i = 0; i < numRows; i++) {
        l.push([]);
    }
    for (let i = 0; i < s.length; i++) {
        l[row].push(s[i])

        if (row == numRows-1) {
            reverse = true
        }
        else if (row == 0) {
            reverse = false;
        }
        if (reverse) {
            row--;
            continue
        }
        row++;
    }

    for (let x = 0; x < l.length; x++) {
        str += l[x].join("")
    }
    return str;
};

console.log(convert("A",1))
