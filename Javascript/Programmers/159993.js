function solution(maps) {
    const n = maps.length;
    const m = maps[0].length;
    let s, l, e;
    for (let i=0; i < n; i++) {
        for (let j=0; j < m; j++) {
            if (maps[i][j] === 'S') {
                s = [i, j, 0]
                break
            } 
        }
    }
    const delta = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    const steps = ['L', 'E'];
    let isEnd = false;

    // 2번 반복
    for (let destination of steps) {
        let q = [s];

        const arr = new Array(m).fill(-1)
        let visited = Array.from({length: n}, (_) => new Array(m).fill(-1))
        let flag = false;

        while (q.length && !flag) {
            const [x, y, cnt] = q.shift();
            visited[x][y] = cnt;
            
            for (let d of delta) {
                let nx = x + d[0], ny = y + d[1];
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && maps[nx][ny] !== "X" && visited[nx][ny] === -1) {
                    if (maps[nx][ny] === destination) {
                        flag = true;
                        s = [nx, ny, cnt+1]
                        if (destination === 'E') {
                            isEnd = true
                        }
                        break
                    }
                    q.push([nx, ny, cnt+1])
                    visited[nx][ny] = cnt + 1
                }
            }
        }
        if (s[2] === 0) return -1
    }
    if (!isEnd) return -1
    return s[2]
    // const result = s[2]
    // if (result === 0 || !isEnd) return -1
    // return result
}
