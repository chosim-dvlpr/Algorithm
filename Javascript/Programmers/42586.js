// dueDates 배열을 순회하며 기준 값보다 큰 값이 나올 때마다 cnt를 answer 배열에 넣고, 리셋
// 7, 3, 9 => 7, 3 / 9 로 나눔

function solution(progresses, speeds) {
    let dueDates = [];
    let answer = [];
    
    for (let i=0; i < progresses.length; i++) {
        let temp = Math.ceil((100 - progresses[i])/speeds[i]);
        dueDates.push(temp);
    }
    
    let standard = dueDates[0];
    let cnt = 1;
    for (let i=1; i < progresses.length; i++) {
        if (dueDates[i] > standard) {
            answer.push(cnt);
            cnt = 1;
            standard = dueDates[i];
            continue
        }
        cnt++;
    }
    answer.push(cnt);
    return answer
}
