function solution(n, computers) {
    let visited = new Array(n).fill(0);
    let cnt = 0;
    
    function dfs(idx) {
        visited[idx] = 1;        
        for (let j=0; j < n; j++) {
            if (idx !== j && computers[idx][j] && !visited[j]) {
                dfs(j);
            }
        }
    }
    
    for (let i=0; i < n; i++) {
        if (!visited[i]) {
            dfs(i);  
            cnt++;
        }
    }
    return cnt;
}
