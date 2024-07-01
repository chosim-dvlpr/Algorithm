function solution(n) {
    const stack = [];
    while (n > 0) {
        if (n % 3 === 0) {
            stack.push('4')
            n = n / 3 - 1
            continue
        }
        stack.push(String(n % 3))
        n = Math.floor(n/3)
    }
    return stack.reverse().join('')
}
