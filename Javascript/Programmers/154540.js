function solution(maps) {
    const n = maps.length
    const m = maps[0].length
    
    const newMaps = []
    maps.forEach((a) => {
        const temp = []
        for (let word of a) {
            temp.push(word)
        }
        newMaps.push(temp)
    })

    const delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    const result = []
    let curr = []

    // 시작점 찾기
    for (let i=0; i<n;i++) {
        for (let j=0; j<m; j++) {
            if (newMaps[i][j] !== 'X') {
                curr = [i, j]
                
                const q = [curr]
                let temp = 0
                temp += Number(newMaps[curr[0]][curr[1]])
                newMaps[curr[0]][curr[1]] = 'X'
                
                while (q.length) {
                    const [x, y] = q.pop()
                    for (let d of delta) {
                        const nx = x + d[0], ny = y + d[1]

                        if (nx >= 0 && nx < n && ny >= 0 && ny < m && newMaps[nx][ny] !== 'X') {
                            temp += Number(newMaps[nx][ny])
                            newMaps[nx][ny] = 'X'
                            q.push([nx, ny])
                        }
                    }
                }
                result.push(temp)
            }
        }
    }
    if (result.length === 0) return [-1]
    return result.sort((a, b) => a - b)
}
