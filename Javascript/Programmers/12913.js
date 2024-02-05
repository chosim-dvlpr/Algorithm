function solution(land) {
    const n = land.length;

    // 이차원 배열 생성
    const arr = Array.from({length : n}, () => Array(4).fill(0));
    arr[0] = land[0];
    
    // (10**5) * 4 * 4
    for (let i=0; i < n-1; i++) { // 행
        for (let j=0; j < 4; j++) { // 현재 행의 열
            for (let k=0; k < 4; k++) { // 다음 행의 열
                if (j !== k) {
                    const temp = arr[i][j] + land[i+1][k]; // 현재까지의 총합 + 다음 행의 원소
                    arr[i+1][k] = Math.max(temp, arr[i+1][k]);
                }
            }
        }
    }
    
    return Math.max(...arr.at(-1))
}
