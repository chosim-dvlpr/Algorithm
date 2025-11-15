const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', (line) => {
  input.push(line.trim())
}).on('close', () => {
  const [_, ...b] = input
  const arr = b.map(Number)
  const stack = []
  arr.forEach((ar) => {
    if (ar === 0) {
      stack.pop()
    } else {
      stack.push(ar)
    }
  })
  console.log(stack.reduce((acc, curr) => acc + curr, 0))
})
