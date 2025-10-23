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
  let len = 0 // 결과
  let cnt = 0 // 제거한수 개수

  // e는 계속 오른쪽으로
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
    len = Math.max(len, e - s + 1 - cnt)
  }

  console.log(len)
})
