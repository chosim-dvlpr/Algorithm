function solution(board) {
    board = board.map(item => item.split(''))
    let answer = 0;
    const n = board.length;
    const m = board[0].length;
    const delta = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    let start;
    
    // 시작점 찾기
    for (let i=0; i < n; i++) {
        for (let j=0; j < m; j++) {
            if (board[i][j] === 'R') {
                start = [i, j]        
            }
        }
    }
    
    const q = [start];

    
    // bfs
    function bfs(idx) {
        
        while (q.length) {
            for (let j=0; j < q.length; j++) {
                
            
            [x, y] = q.shift(); // popleft
            board[x][y] = 0
            console.log('시작', x, y)

            for (let i=0; i < delta.length; i++) {
                let nx = x + delta[i][0];
                let ny = y + delta[i][1];                    
                while (0 <= nx && nx < n && 0 <= ny && ny < m && board[nx][ny] !== 'D') {
                    nx += delta[i][0];
                    ny += delta[i][1];
                }
                nx -= delta[i][0];
                ny -= delta[i][1];
                
                if (board[nx][ny] === 'G') return answer++;
                if (board[nx][ny] !== 0) {
                    board[nx][ny] = 0;
                    q.push([nx, ny])
                    console.log('q 업뎃 ', q)
                }
                
            }    
            answer++;
            console.log('answer : ', answer)
            console.log('')
            }
        }        
    }
    
    bfs(start)
    
    
    return -1
}
