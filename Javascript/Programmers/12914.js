function solution(n) {
    let dp = new Array(n+1).fill(0);
    const m = 1234567;
    
    dp[1] = 1;
    dp[2] = 2;
    
    for (let i=3; i < n+1; i++) {
        dp[i] = (dp[i-2] + dp[i-1]) % m; // % 연산은 중간에 나머지를 구해도 결과는 같음
    }
    
    return dp[n];
}
