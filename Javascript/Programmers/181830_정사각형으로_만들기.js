function solution(arr) {
    const row = arr.length;
    const col = arr[0].length;
    
    if (row > col) {
        let add = row - col;
        for (let i=0; i < row; i++) {
            for (let j=0; j < add; j++) {
                arr[i].push(0)            
            }
        }
    } else if (row < col) {
        let add = col - row;
        let ar = new Array(col).fill(0)
        for (let i=0; i<add; i++) {
            arr.push(ar)
        }
    }
    return arr
}
