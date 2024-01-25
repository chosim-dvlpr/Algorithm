function solution(people, limit) {
    people = people.sort((a, b) => a - b);
    const n = people.length;
    let i = 0;
    let j = n - 1;
    let cnt = n; // cnt의 최댓값은 배열의 길이만큼
    
    while (i < j) {
        if (people[i] + people[j] <= limit) {
            cnt--; // 합계가 limit 이하인 경우 cnt를 1 감소시킴
            // 배열이 오름차순이므로 i+1은 i보다 크거나 같을 것이고
            // j-1은 j보다 작거나 같을 것
            // j+1은 j보다 클 것이므로
            // i+1와 j+1을 합하면 limit보다 커지게 됨
            // 따라서 j-1로 새롭게 while문 진행
            i++;
            j--; 
            continue
        }
        j--;
    }
    return cnt;
}
