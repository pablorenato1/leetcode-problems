// Remember to redo this problem

/**
 * @param {number} n
 * @return {number}
 */
 var numSquares = function(n) {
    var bestSeq = n;
    // console.log(bestSeq)
    var num = []
    // console.log(1)
    for (let i = 1; i < n; i++) {
        if ((i*i > n)) break
        num.push(i*i)
    }
    console.log(num)
    var findSeq = (p) => {
        console.log(p)
        if (0 > (num.length+p)) return n
        console.log(1)
        var temp = []
        for (let x = num.length-p; x >= 0; x--) {
            while (true) {
                if ((temp.reduce((partialSum, a) => partialSum + a, 0)+num[x]) > n || temp.length > bestSeq) break
                temp.push(num[x])
            }
            // console.log(temp)
        }
        return Math.min(temp.length, findSeq(p+1))
    }
    // for (let a = 1; a < num.length+1; a++) {
    //     var qt = findSeq(a)
    //     if (qt < bestSeq) bestSeq = qt;
    // }
    return findSeq(1)//bestSeq
};

console.log(numSquares(12))