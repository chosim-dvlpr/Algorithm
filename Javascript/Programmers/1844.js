function solution(maps) {
    const n = maps.length;
    const m = maps[0].length;
    
    const delta = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    const start = [0, 0]
    const end = [n-1, m-1]
    const queue = [[...start, 1]]
    maps[start[0]][start[1]] = 0
    let result = 9876542310;
    
    while (queue.length) {
        const [x, y, cnt] = queue.shift();
        
        if (cnt >= result) continue;

        for (let [dx, dy] of delta) {
            const nx = x + dx, ny = y + dy;
            if (nx >= 0 && nx < n && ny >= 0 && ny < m && maps[nx][ny] === 1) {
                maps[nx][ny] = 0
                if (nx === end[0] && ny === end[1]) {
                    if (result > cnt+1) {
                        result = cnt+1
                    }
                } else {
                    queue.push([nx, ny, cnt+1])    
                }
            }
        }
    }
    
    
    if (result <= n*m) return result;
    return -1;
}
