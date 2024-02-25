function solution(n) {
    let result = Array.from(({length: n}), (_, index) => new Array(index+1).fill(0));
    let i = 0, j = 0;
    let prev = 1;
    let mx = n * (n + 1) / 2;
    while (prev < mx + 1) {
        // 아래로
        while (i < n && !result[i][j]) {
            result[i][j] = prev++
            i += 1
        }
        i -= 1
        j += 1
        
        // 오른쪽으로
        while (j < n && !result[i][j]) {
            result[i][j] = prev++;
            j += 1
        }
        j -= 2
        i -= 1
        
        // 위로
        while (i > 0 && j > 0 && !result[i][j]) {
            result[i][j] = prev++;
            i -= 1
            j -= 1
        }
        i += 2
        j += 1        
    }
    
    
    
    return result.flat()
}
