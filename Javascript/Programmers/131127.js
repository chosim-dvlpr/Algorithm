function solution(want, number, discount) {
    const n = discount.length;
    let result = 0;
    
    for (let start=0; start < n - 9; start++) {
        let wantMap = new Map();
        for (let i in want) {
            wantMap.set(want[i], number[i])
        }
        const arr = discount.slice(start, start+10)
        
        for (let a of arr) {
            if (!wantMap.has(a)) break
            
            const remains = wantMap.get(a);
            if (remains > 0) {
                wantMap.set(a, remains-1)    
            } else break
        }
        let flag = true
        for (let [key, value] of wantMap) {
            if (value !== 0) {
                flag = false
                break
            }
        }
        if (flag) {
            result++    
        }
    }
    return result;
}
