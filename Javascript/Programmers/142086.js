// 가장 가까운 같은 글자

function solution(s) {
    let obj = {}
    let answer = []
    for (let i=0; i < s.length; i++) {
        const keys = Object.keys(obj)
        
        if (keys.includes(s[i])) {
            answer.push(i-obj[s[i]])
        } else {
            answer.push(-1)    
        }
        obj[s[i]] = i
    }
    return answer
}
