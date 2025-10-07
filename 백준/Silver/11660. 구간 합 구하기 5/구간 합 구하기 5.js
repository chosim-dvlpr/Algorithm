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
  const arr = []
  const tc = []
  const result = []

  for (let i = 0; i < n; i++) {
    const a = b[i].split(' ').map(Number)
    arr.push(a)
  }

  for (let i = n; i < n + m; i++) {
    const [x1, y1, x2, y2] = b[i].split(' ').map(Number)
    tc.push([x1 - 1, y1 - 1, x2 - 1, y2 - 1])
  }

  const sums = Array.from({ length: n }, () => Array(n).fill(0))
  sums[0][0] = arr[0][0]

  for (let j = 1; j < n; j++) {
    sums[0][j] = sums[0][j - 1] + arr[0][j]
  }
  for (let i = 1; i < n; i++) {
    sums[i][0] = sums[i - 1][0] + arr[i][0]
  }

  for (let i = 1; i < n; i++) {
    for (let j = 1; j < n; j++) {
      sums[i][j] =
        sums[i - 1][j] + sums[i][j - 1] - sums[i - 1][j - 1] + arr[i][j]
    }
  }

  for (let [x1, y1, x2, y2] of tc) {
    let s = sums[x2][y2]
    if (y1 > 0) {
      s -= sums[x2][y1 - 1]
    }
    if (x1 > 0) {
      s -= sums[x1 - 1][y2]
    }
    if (x1 > 0 && y1 > 0) {
      s += sums[x1 - 1][y1 - 1]
    }
    result.push(s)
  }

  console.log(result.join('\n'))
})
