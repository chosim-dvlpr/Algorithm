const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', (line) => {
  input.push(line.trim())
}).on('close', () => {
  // BFS
  // 2를 만나면 바로 통과
  const [a, ...ar] = input
  const [n, m, t] = a.split(' ').map(Number)
  const arr = ar.map((input) => input.split(' ').map(Number))
  const times = Array.from({ length: n }, () => Array(m).fill(Infinity))
  const start = [0, 0]
  times[start[0]][start[1]] = 0

  const q = [[...start, false]]
  const delta = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ]
  let result = Infinity
  let flag = false
  while (q.length > 0) {
    const [x, y, hasSword] = q.shift()

    if (flag) break

    for (let [dx, dy] of delta) {
      const nx = x + dx,
        ny = y + dy

      if (flag) break

      if (
        0 <= nx &&
        nx < n &&
        0 <= ny &&
        ny < m &&
        times[nx][ny] > times[x][y] + 1 &&
        times[x][y] + 1 <= t
      ) {
        if (!hasSword && arr[nx][ny] === 1) continue
        times[nx][ny] = times[x][y] + 1
        if (nx === n - 1 && ny === m - 1) {
          // 성공
          result = Math.min(result, times[nx][ny])
          flag = true
          break
        }
        if (arr[nx][ny] === 2) {
          const sums = times[nx][ny] + (n - 1 - nx) + (m - 1 - ny)
          if (sums <= t) {
            result = sums
            continue
          }
        }
        q.push([nx, ny, hasSword])
      }
    }
  }
  console.log(result === Infinity ? 'Fail' : result)
})
