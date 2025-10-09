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
  const n = Number(a)
  const arr = b.map((ar) => ar.split(' ').map(Number))

  for (let k = 0; k < n; k++) {
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (arr[i][k] && arr[k][j]) {
          arr[i][j] = 1
        }
      }
    }
  }

  for (let ar of arr) {
    console.log(ar.join(' '))
  }
})
