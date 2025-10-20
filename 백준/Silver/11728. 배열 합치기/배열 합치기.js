const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', (line) => {
  input.push(line.trim())
}).on('close', () => {
  // nlogn => 10**6 * 6
  const [k, a, b] = input
  const [n, m] = k.split(' ').map(Number)
  const arrA = a.split(' ').map(Number)
  const arrB = b.split(' ').map(Number)

  let ai = 0
  let bi = 0
  let result = []
  while (ai < n && bi < m) {
    if (arrA[ai] < arrB[bi]) {
      result.push(arrA[ai])
      ai++
    } else {
      result.push(arrB[bi])
      bi++
    }
  }

  if (ai < n) {
    result = [...result, ...arrA.splice(ai)]
  } else {
    result = [...result, ...arrB.splice(bi)]
  }

  console.log(result.join(' '))
})
