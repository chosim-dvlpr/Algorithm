function solution(sizes) {
    let maxA = 0;
    let maxB = 0;
    
    sizes.forEach((size, i) => {
        let temp = 0;
        let tempRev = 0;
        temp = Math.abs(maxA - size[0]) + Math.abs(maxB - size[1])
        tempRev = Math.abs(maxA - size[1]) + Math.abs(maxB - size[0])
        if (temp < tempRev) {
            maxA = Math.max(maxA, size[0])
            maxB = Math.max(maxB, size[1])
        } else {
            maxA = Math.max(maxA, size[1])
            maxB = Math.max(maxB, size[0])
        }
    })
    return maxA * maxB;
}
