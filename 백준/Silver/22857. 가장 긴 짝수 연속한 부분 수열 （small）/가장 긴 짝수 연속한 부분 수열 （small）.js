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
  const [n, k] = a.split(' ').map(Number)
  const arr = b.split(' ').map(Number)
  let s = 0
  let cnt = 0
  let result = 0

  for (let e = 0; e < n; e++) {
    if (arr[e] % 2 === 1) {
      cnt++
    }
    while (cnt > k) {
      if (arr[s] % 2 === 1) {
        cnt--
      }
      s++
    }
    result = Math.max(result, e - s + 1 - cnt)
  }

  console.log(result)
})
