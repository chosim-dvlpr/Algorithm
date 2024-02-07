function solution(number, k) {
    let stack = [];
    const n = number.length;
    
    for (let i=0; i < n; i++) {
        while (k > 0 && number[i] > stack.at(-1)) { // 현재 숫자와 스택의 마지막 숫자 비교
            stack.pop();
            k--;
        }
         // 현재 스택의 길이가 구해야 하는 길이(n-k) 보다 짧다면 스택에 추가
        if (stack.length < n-k) {
            stack.push(number[i])
        }
    }
    return stack.join('')
}
