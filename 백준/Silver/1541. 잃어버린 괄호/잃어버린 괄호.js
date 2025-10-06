const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', (line) => {
  input.push(line.trim())
}).on('close', () => {
  // 값을 최소로 만들기
  // - 기준
  const a = String(input)
  const calc = a.split('-')
  // 첫 번째 문자 - 확인
  let result = 0
  const c = calc[0].split('+').map(Number)
  const sums = c.reduce((acc, curr) => acc + curr, 0)
  if (a[0] === '-') {
    result -= sums
  } else {
    result += sums
  }
  for (let i = 1; i < calc.length; i++) {
    const arr = calc[i].split('+').map(Number)
    result -= arr.reduce((acc, curr) => acc + curr, 0)
  }
  console.log(result)
})
