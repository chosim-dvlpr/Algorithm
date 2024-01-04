function solution(board) {
    board = board.map(item => item.split(''));
    let answer = 0;
    const n = board.length;
    const m = board[0].length;
    const delta = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    let q = [];
    
    // 시작점 찾기
    for (let i=0; i < n; i++) {
        for (let j=0; j < m; j++) {
            if (board[i][j] === 'R') {
                q.push([i, j]);
                break;
            }
        }
    }
    
    // bfs
    while (q.length) {
        const size = q.length; // q의 길이가 계속 변하므로 고정시킴
        
        for (let j=0; j < size; j++) {
            [x, y] = q.shift(); // popleft
            board[x][y] = 0 // 방문표시

            // 4방향 확인
            for (let i=0; i < delta.length; i++) {
                let nx = x + delta[i][0];
                let ny = y + delta[i][1];
                // 범위 내에 있거나 D가 나오지 않을 때까지 계속 같은 방향 이동
                while (0 <= nx && nx < n && 0 <= ny && ny < m && board[nx][ny] !== 'D') {
                    nx += delta[i][0];
                    ny += delta[i][1];
                }
                nx -= delta[i][0];
                ny -= delta[i][1];
                // 끝이나 벽에 닿았을 때
                if (board[nx][ny] === 'G') return answer+1
                if (board[nx][ny] !== 0) {
                    board[nx][ny] = 0; // 방문표시
                    q.push([nx, ny]) // 새롭게 이동할 좌표 q에 담기
                }
            }    
        }
        answer++; // 네 방향 확인 다 하면 +1
    }            
    return -1
}
