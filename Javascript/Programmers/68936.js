function solution(arr) {
    if (arr.every(row => row.every(cell => cell === 0))) return [1, 0]
    if (arr.every(row => row.every(cell => cell === 1))) return [0, 1]
    
    const answer = [0, 0]
    
    function divider(row, col, len) {
        if (len === 1) {
            answer[arr[row][col]]++
            return
        }
        
        let flag = true
        for (let i=row; i < row+len; i++) {
            for (let j=col; j < col+len; j++) {
                if (arr[i][j] !== arr[row][col]) {
                    flag = false
                }
            }
        }
        
        if (flag) {
            answer[arr[row][col]]++
            return
        }
        const half = parseInt(len/2)

        divider(row, col, half)
        divider(row, col + half, half)
        divider(row + half, col, half)
        divider(row + half, col + half, half)
    }
    
    divider(0, 0, arr.length)
    
    return answer
}
