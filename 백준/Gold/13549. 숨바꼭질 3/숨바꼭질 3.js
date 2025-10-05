const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', (line) => {
  input.push(line.trim())
}).on('close', () => {
  const [n, k] = String(input).split(' ').map(Number)
  if (n === k) {
    console.log(0)
    return
  }
  const LIMIT = 100000
  const dp = Array(LIMIT + 1).fill(Infinity)
  const q = [n]
  dp[n] = 0
  while (q.length > 0) {
    const index = q.shift()

    if (index === k) {
      break
    }
    if (index * 2 <= LIMIT && dp[index] < dp[index * 2]) {
      dp[index * 2] = dp[index]
      q.push(index * 2)
    }
    if (index + 1 <= LIMIT && dp[index] + 1 < dp[index + 1]) {
      dp[index + 1] = dp[index] + 1
      q.push(index + 1)
    }
    if (index - 1 >= 0 && dp[index] + 1 < dp[index - 1]) {
      dp[index - 1] = dp[index] + 1
      q.push(index - 1)
    }
  }
  console.log(dp[k])
})
