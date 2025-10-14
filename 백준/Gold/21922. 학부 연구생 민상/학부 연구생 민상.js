const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', (line) => {
  input.push(line.trim())
}).on('close', () => {
  // 9 : 에어컨
  // 1: 좌우 바람은 막힘
  // 2: 상하 바람은 막힘
  // 3: 90도 (방향이 위쪽 -> 오른쪽으로 / 아래쪽 -> 왼쪽으로 / 오른쪽으로 -> 위쪽으로 / 왼쪽 -> 아래쪽)
  // 4: 90도 (위쪽 -> 왼 / 아래쪽 -> 오른쪽 / 오른쪽 -> 아래쪽 / 왼쪽 -> 위쪽)
  const [a, ...b] = input
  const [n, m] = a.split(' ').map(Number)
  const arr = b.map((ar) => ar.split(' ').map(Number))
  const visited = Array.from({ length: 4 }, () =>
    Array.from({ length: n }, () => Array(m).fill(false))
  )
  const cooled = Array.from({ length: n }, () => Array(m).fill(false))
  let cnt = 0
  // const q = []

  const delta = [
    [0, -1],
    [0, 1],
    [-1, 0],
    [1, 0],
  ] // 왼쪽을 향하는 바람, 오른쪽 향함, 위쪽 향함, 아래족 향함

  // let index = 0

  // 에어컨 찾기
  // const acs = []
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (arr[i][j] === 9) {
        cooled[i][j] = true
        for (let k = 0; k < 4; k++) {
          // q.push([i, j, k])
          // visited[k][i][j] = true
          let x = i,
            y = j,
            dir = k
          while (1) {
            const nx = x + delta[dir][0],
              ny = y + delta[dir][1]
            if (0 > nx || 0 > ny || n <= nx || m <= ny) break

            const currItem = arr[nx][ny]
            let nextDir = dir

            if (currItem === 1) {
              // 좌우반전
              // if (dir === 0 || dir === 1) continue
              if (dir === 0) {
                nextDir = 1
              } else if (dir === 1) {
                nextDir = 0
              }
            } else if (currItem === 2) {
              // 상하반전
              // if (dir === 2 || dir === 3) continue
              if (dir === 2) {
                nextDir = 3
              } else if (dir === 3) {
                nextDir = 2
              }
            } else if (currItem === 3) {
              if (dir === 0) {
                // 왼 -> 아래
                nextDir = 3
              } else if (dir === 1) {
                // 오 -> 위
                nextDir = 2
              } else if (dir === 2) {
                // 위 -> 오
                nextDir = 1
              } else if (dir === 3) {
                // 아래 -> 왼
                nextDir = 0
              }
            } else if (currItem === 4) {
              if (dir === 0) {
                // 왼 -> 위
                nextDir = 2
              } else if (dir === 1) {
                // 오 -> 아래
                nextDir = 3
              } else if (dir === 2) {
                // 위 -> 왼
                nextDir = 0
              } else if (dir === 3) {
                // 아래 -> 오
                nextDir = 1
              }
            }

            if (visited[nextDir][nx][ny]) break

            visited[nextDir][nx][ny] = true
            cooled[nx][ny] = true
            x = nx
            y = ny
            dir = nextDir
          }
        }
      }
    }
  }

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (cooled[i][j]) {
        cnt++
      }
    }
  }
  console.log(cnt)
})
