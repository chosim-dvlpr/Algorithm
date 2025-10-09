const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', (line) => {
  input.push(line.trim())
}).on('close', () => {
  const [a, ...b] = input
  const [n, m] = a.split(' ').map(Number)
  const arr = b.map((a) => a.split(' ').map(Number))
  const dp = []

  for (let i = 0; i < n; i++) {
    dp.push([])
  }
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      dp[i].push(Array(3).fill(Infinity))
    }
  }
  // dp[0][0][1] = 1

  for (let i = 0; i < m; i++) {
    dp[0][i] = Array(3).fill(arr[0][i])
  }

  const delta = [
    [1, -1, 0],
    [1, 0, 1],
    [1, 1, 2],
  ]

  for (let i = 0; i < n - 1; i++) {
    for (let j = 0; j < m; j++) {
      for (let [dx, dy, nextDir] of delta) {
        const nx = i + dx,
          ny = j + dy
        if (0 <= ny && ny < m) {
          for (let d = 0; d < 3; d++) {
            if (d === nextDir) continue

            dp[nx][ny][nextDir] = Math.min(
              dp[nx][ny][nextDir],
              arr[nx][ny] + dp[i][j][d]
            )
          }
        }
      }
    }
  }
  let result = Infinity
  for (let i = 0; i < m; i++) {
    result = Math.min(...dp[n - 1][i], result)
  }
  console.log(result)
})
