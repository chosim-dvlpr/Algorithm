function solution(priorities, location) {
    priorities.forEach((p, i) => {
        priorities[i] = [p, i]
    })
    
    let answer = [];
    while (priorities.length > 0) {
        const n = priorities.length;
        let flag = 0;
        for (let i=1; i < n; i++) {
            // 더 큰 우선순위 값이 있을 때
            if (priorities[0][0] < priorities[i][0]) {
                priorities.push(priorities.shift())
                flag = 1;
                break
            }
        }
        if (flag === 0) {
            // 가장 큰 우선순위 값일 때
            answer.push(priorities.shift())
        }
    }
    let res = 0;
    answer.forEach((a, i) => {
        if (a[1] === location) res = i+1;
    })
    return res
}
