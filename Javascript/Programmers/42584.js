function solution(prices) {
    const n = prices.length;
    let stack = [];
    let times = new Array(n).fill(0)

    for (let i=0; i < n; i++) {
        stack.forEach((s, i) => {
            times[s[1]] += 1
        })
        while (stack.length && stack[stack.length-1][0] > prices[i]) {
            stack.pop();
        }
        stack.push([prices[i], i]);
    }
    return times
}
