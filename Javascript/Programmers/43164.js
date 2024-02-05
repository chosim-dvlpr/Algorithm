function solution(tickets) {
    let answer = [];
    const result = [];
    const visited = [];

    // 알파벳 순으로 정렬
    tickets.sort();

    const n = tickets.length;
    function dfs(start, count) {
        result.push(start);

        if (count === n) {
            answer = result;
            return true;
        }

        for (let i=0; i < n; i++) {
            // i번째를 방문하지 않은 상태고, i번째의 왼쪽 문자가 start와 같을 때
            if (!visited[i] && tickets[i][0] === start) {
                visited[i] = true; // 방문 표시
                // 해당 배열의 도착지를 다시 시작점으로 한 뒤 dfs 실행
                if (dfs(tickets[i][1], count+1)) {
                    return true;
                }
                visited[i] = false; // 방문 표시 되돌림
            }       
        }
        // 더이상 갈 곳이 없는 상태라면 최근 방문했던 지점을 result에서 빼냄
        result.pop();
        
        return false;
    }
    
    dfs("ICN", 0);
    return answer;
}
