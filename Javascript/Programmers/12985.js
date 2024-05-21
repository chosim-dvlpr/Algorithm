function solution(n,a,b) {
    let result = 0
    while (a !== b) {
        a = parseInt((a+1) / 2, 10)
        b = parseInt((b+1) / 2, 10)
        result++
    }
    return result
}
