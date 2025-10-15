const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', (line) => {
  input.push(line.trim())
}).on('close', () => {
  const [_, b, ...c] = input
  const str = String(b)
  const num = c.map(Number)
  const nums = []
  const CALC = {
    '+': true,
    '-': true,
    '/': true,
    '*': true,
  }
  const stack = []

  for (let s of str) {
    nums.push(s)
  }

  for (let s of nums) {
    if (CALC[s]) {
      const b = stack.pop()
      const a = stack.pop()
      if (s === '+') {
        stack.push(a + b)
      } else if (s === '-') {
        stack.push(a - b)
      } else if (s === '/') {
        stack.push(a / b)
      } else if (s === '*') {
        stack.push(a * b)
      }
    } else {
      stack.push(num[s.charCodeAt() - 65])
    }
  }
  console.log(stack[0].toFixed(2))
})
