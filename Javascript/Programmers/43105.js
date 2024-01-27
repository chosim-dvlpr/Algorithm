function solution(triangle) {
    const n = triangle.length;
    
    for (let i=1; i < n; i++) {
        let m = triangle[i].length;
    
        for (let j=0; j < m; j++) {
            if (j === 0) {
                triangle[i][j] = triangle[i-1][0] + triangle[i][j]
            } else if (j === m - 1) {
                triangle[i][j] = triangle[i-1][triangle[i-1].length - 1] + triangle[i][j]
            } else {
                triangle[i][j] = Math.max(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j]
            }
        }
    }    
    return Math.max(...triangle[n-1])
}
