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
  const arr = b.map((a) => a)
  const finished = new Map()
  for (let i = 0; i < n; i++) {
    if (finished.has(arr[i])) {
      finished.set(arr[i], finished.get(arr[i]) + 1)
    } else {
      finished.set(arr[i], 1)
    }
  }

  for (let i = n; i < arr.length; i++) {
    if (finished.has(arr[i])) {
      finished.set(arr[i], finished.get(arr[i]) - 1)
      if (finished.get(arr[i]) === 0) {
        finished.delete(arr[i])
      }
    }
  }
  const key = [...finished.keys()]
  key.forEach((k) => console.log(k))
})
