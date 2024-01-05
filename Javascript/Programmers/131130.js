function solution(cards) {
    const n = cards.length;
    let cardsCountList = [];
    let visited = new Array(n).fill(0);
    let idx = 0;
    let cnt = 0;
    let flag = true;

    while (flag) {
        for (let i=0; i < n; i++) {
            if (visited[idx] === 1) {
                cnt !== 0 && cardsCountList.push(cnt); // 순회를 한 경우(cnt !== 0)만 배열에 저장
                idx = i; // 다음 인덱스로 넘어가기
                cnt = 0;
                continue
            }
            visited[idx] = 1;
            idx = cards[idx] - 1;
            cnt++;
        }
        
        // 하나라도 방문하지 않은 상자가 있다면 반복
        flag = false;
        for (let j=0; j < n; j++) {
            if (visited[j] === 0) {
                flag = true;
                break
            }
        }
    }
    if (cardsCountList.length < 2) {
        return 0
    }
    cardsCountList.sort((a, b) => b - a); // 내림차순 정렬
    return cardsCountList[0] * cardsCountList[1]
}
