function solution(k, tangerine) {
    const match = new Map();
    
    for (let t of tangerine) {
        if (!match.has(t)) {
            match.set(t, 1)
            continue
        }
        match.set(t, match.get(t)+1)
    }
    
    const stack = [];
    for (let [t, count] of match) {
        stack.push([count, t])
    }
    
    stack.sort((a, b) => b[0] - a[0])
    
    let result = 0;
    let cnt = 0;

    for (let s of stack) {
        result += s[0];
        cnt++;
        if (result >= k) {
            return cnt
        }
    }
}
