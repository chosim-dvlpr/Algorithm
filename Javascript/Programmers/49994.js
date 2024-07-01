function solution(dirs) {
    const delta = {
        U: [0, 1],
        D: [0, -1],
        R: [1, 0],
        L: [-1, 0]
    }
    let curr = [0, 0]
    let result = 0;
    const arr = []
    const equals = (a, b) => JSON.stringify(a) === JSON.stringify(b);
    
    for (let dir of dirs) {
        const d = delta[dir]
        const nx = curr[0]+d[0], ny = curr[1]+d[1]
        if (nx > 5 || nx < -5 || ny > 5 || ny < -5) continue
        
        const position = [...curr, nx, ny]
        let flag = true
        
        for (let [a,b,c,d] of arr) {
            if ((equals([a,b],curr) && equals([c,d], [nx, ny])) || (equals([c, d], curr) && equals([a, b], [nx, ny]))) {
                flag = false
            }
        }
        if (flag) {
            arr.push(position)
            result++;
        }
        curr = [nx, ny]
    }
    return result
}
