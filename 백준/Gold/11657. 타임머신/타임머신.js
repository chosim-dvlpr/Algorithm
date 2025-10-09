const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', (line) => {
  input.push(line.trim())
}).on('close', () => {
  // 시작: 1번
  const [a, ...b] = input
  const [n, m] = a.split(' ').map(Number)
  const times = Array.from({ length: n + 1 }, () => Infinity)
  times[1] = 0
  const edges = []

  b.forEach((ar) => {
    edges.push(ar.split(' ').map(Number))
  })

  for (let i = 0; i < n - 1; i++) {
    for (let [start, end, cost] of edges) {
      if (times[start] !== Infinity && times[end] > times[start] + cost) {
        times[end] = times[start] + cost
      }
    }
  }

  for (let [start, end, cost] of edges) {
    if (times[end] > times[start] + cost) {
      console.log(-1)
      return
    }
  }

  for (let i = 2; i < n + 1; i++) {
    console.log(times[i] === Infinity ? -1 : times[i])
  }
})
