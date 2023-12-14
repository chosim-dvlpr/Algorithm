function solution(s) {    
    const words = {'[': ']', '{': '}', '(': ')'};
    let cnt = 0;
    let str = s;
    // 올바른지 확인
    for (let i=0; i < s.length; i++) {
        // 문자열 회전
        let newStr = str.substring(i, s.length) + str.substring(0, i)
        let stack = new Array();
        let flag = true;
        // 회전된 문자열 순회
        for (let j=0; j < newStr.length; j++) {
            const keys = Object.keys(words) // 열린 괄호만 포함하는 key 배열
            const s = newStr[j]
            if (keys.includes(s)) { // 열린 괄호일 때 (현재 문자가 keys에 속할 때)
                stack.push(s)
            } else { // 닫힌 괄호일 때 (keys에 속하지 않을 때)
                const word = stack.pop() // stack이 비어있다면 undefined 출력
                if (word === undefined || words[word] !== s) {
                    flag = false;
                    break; // for ~ j문 종료
                }            
            }
        }
        if (stack.length === 0 && flag) {cnt++};
    }
    return cnt
}
