function solution(s) {
    let tuples = [];
    let temp = [];
    const n = s.length;
    
    let start = 1, end = 1;
    for (let i=1; i < n-1; i++) {
        if (s[i] === '{') {
            start = i+1;
        } else if (s[i] === '}') {
            end = i;
            temp = s.substring(start, end).split(',').map(Number)
            tuples.push(temp)
        }        
    }
    tuples.sort((a, b) => a.length - b.length);
    
    let result = [];
    tuples.forEach((tuple) => {
        tuple.forEach((t) => {
            if (!result.includes(t)) {
                result.push(t)
            }
        })
    })
    return result
}
