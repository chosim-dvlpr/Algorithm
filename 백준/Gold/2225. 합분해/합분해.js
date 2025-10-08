const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', (line) => {
  input.push(line.trim())
}).on('close', () => {
  const [n, k] = input[0].split(' ').map(Number)
  const dp = Array.from({ length: k + 1 }, () => Array(n + 1).fill(1))
  const DIVIDER = 1000000000

  for (let i = 1; i < k + 1; i++) {
    for (let j = 1; j < n + 1; j++) {
      dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000000
    }
  }
  console.log(dp[k - 1][n] % DIVIDER)
})
