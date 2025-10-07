const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', (line) => {
  input.push(line.trim())
}).on('close', () => {
  const n = Number(input[0])
  const dp = Array(n + 1).fill(0)
  const DIVIDER = 10007
  dp[1] = 1
  dp[2] = 2
  if (n < 3) {
    console.log(dp[n] % DIVIDER)
    return
  }
  for (let i = 3; i < n + 1; i++) {
    dp[i] = (dp[i - 2] + dp[i - 1]) % DIVIDER
  }
  console.log(dp[n] % DIVIDER)
})
