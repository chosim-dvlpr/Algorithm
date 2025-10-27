const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', (line) => {
  input.push(line.trim())
}).on('close', () => {
  const [a, b] = input
  const [n, m] = a.split(' ').map(Number)
  const nums = b.split(' ').map(Number)
  let len = Infinity
  let s = 0
  let sums = 0
  for (let e = 0; e < n; e++) {
    sums += nums[e]

    while (sums >= m) {
      len = Math.min(len, e - s + 1)
      sums -= nums[s]
      s++
    }
  }

  console.log(len === Infinity ? 0 : len)
})
