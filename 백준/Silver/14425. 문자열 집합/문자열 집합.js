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
  const s = new Map()
  let cnt = 0
  for (let i = 0; i < n; i++) {
    s.set(b[i], true)
  }
  for (let i = n; i < n + m; i++) {
    if (s.has(b[i])) {
      cnt++
    }
  }
  console.log(cnt)
})
