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
  const [n, k] = a.split(' ').map(Number)
  const arr = b.map((ar) => ar.split(' ').map(Number))
  const dp = Array.from({ length: k + 1 }, () => 0)

  for (let i = 0; i < n; i++) {
    // i: 물품
    const [w, v] = arr[i]
    for (let j = k; j >= w; j--) {
      // j: 무게 한도
      dp[j] = Math.max(dp[j], dp[j - w] + v)
    }
  }
  console.log(dp[k])
})
