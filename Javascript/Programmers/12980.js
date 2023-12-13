// n에서 숫자를 줄여나가는 방식 사용
// -> n이 0이 될 때까지 반복
function solution(n) {
    let answer = 0;
    while (n !== 0) {
        if (n%2 === 0) { // 짝수일 때는 순간이동 하는 것이 유리
            n /= 2;
            continue
        } // 홀수일 때는 n을 1씩 감소, answer를 1씩 증가시킴
        n--;
        answer++;
    }
    return answer;
}
