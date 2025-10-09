const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', (line) => {
  input.push(line.trim())
}).on('close', () => {
  const [a, _, ...c] = input
  const n = Number(a)
  const arr = Array.from({ length: n }, () => Array(n).fill(Infinity))
  c.forEach((ar) => {
    const [a, b, c] = ar.split(' ').map(Number)
    arr[a - 1][b - 1] = Math.min(arr[a - 1][b - 1], c)
  })

  for (let k = 0; k < n; k++) {
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (i === j) continue
        arr[i][j] = Math.min(arr[i][j], arr[i][k] + arr[k][j])
      }
    }
  }
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (arr[i][j] === Infinity) {
        arr[i][j] = 0
      }
    }
    console.log(arr[i].join(' '))
  }
})
