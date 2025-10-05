const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', (line) => {
  input.push(line.trim())
}).on('close', () => {
  // 0 : 불가
  // 1 : 이동 가능
  // 2 : 목표 지점
  const [a, ...ar] = input
  const [n, m] = a.split(' ').map(Number)
  const arr = ar.map((a) => a.split(' ').map(Number))
  const result = Array.from({ length: n }, () => Array(m).fill(-1))

  // 시작지점 찾기
  const start = [0, 0]
  for (let i = 0; i < n; i++) {
    let flag = false
    for (let j = 0; j < m; j++) {
      if (arr[i][j] === 2) {
        start[0] = i
        start[1] = j
        flag = true
        break
      }
    }
    if (flag) break
  }

  function bfs() {
    result[start[0]][start[1]] = 0
    const q = [start]
    const delta = [
      [0, 1],
      [0, -1],
      [1, 0],
      [-1, 0],
    ]
    while (q.length > 0) {
      const [x, y] = q.shift()
      for (let [dx, dy] of delta) {
        const nx = x + dx,
          ny = y + dy
        if (0 <= nx && nx < n && 0 <= ny && ny < m && arr[nx][ny] === 1) {
          result[nx][ny] = result[x][y] + 1
          arr[nx][ny] = 0
          q.push([nx, ny])
        }
      }
    }
  }
  bfs()
  // 도달할 수 없는 위치는 -1로 변환
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (arr[i][j] === 0 && result[i][j] === -1) {
        result[i][j] = 0
      }
    }
  }
  for (let r of result) {
    console.log(r.join(' '))
  }
})
