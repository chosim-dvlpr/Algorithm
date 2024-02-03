function solution(gems) {
    const n = gems.length;
    const setGems = new Set(gems);
    const m = setGems.size;

    // 배열에 중복이 없을 때와 문자열이 하나만 있는 경우
    // 주석처리 해도 잘 통과됨
//     if (n === m || m === 1) {
//         return [1, m]
//     }
    
    let mn = n+1;
    let gemsMap = new Map();
    let e = 0, s = 0, mnStart = 0;
    
    while (e < n) {
        if (!gemsMap.has(gems[e])) {
            gemsMap.set(gems[e], 1);
        } else {
            gemsMap.set(gems[e], gemsMap.get(gems[e]) + 1);
        }
        
        // 모든 원소를 한개 이상씩 다 모았을 때
        while (gemsMap.size === m) {
            // 구간 길이가 mn보다 짧을 때
            if (e - s < mn) {
                mn = e - s;
                mnStart = s;
            }

            // 해당 문자열의 숫자 감소
            gemsMap.set(gems[s], gemsMap.get(gems[s]) - 1);

            // 해당 문자열이 구간 내에 더이상 존재하지 않게 되면 key를 지움
            if (gemsMap.get(gems[s]) === 0) {
                gemsMap.delete(gems[s]);
            }
            s++; // 시작점을 1씩 증가
        }
        e++; // 종료점을 1씩 증가하며 새로운 문자열 탐색
    }
    return [mnStart+1, mnStart+mn+1]
}
