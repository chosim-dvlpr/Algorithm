function solution(operations) {
    let arr = [];
    for (let i=0; i < operations.length; i++) {
        const word = operations[i].split(' ')[0]
        const num = operations[i].split(' ')[1]
        if (word === 'I') {
            arr.push(num)
            arr.sort((a, b) => a - b);
            continue
        }
        if (num === '-1') { // 최솟값 삭제
            arr.shift()
            continue
        }
        arr.pop() // 최댓값 삭제
    }
    if (arr.length > 0) {
        return [Number(arr[arr.length-1]), Number(arr[0])]
    }
    return [0, 0]
}
