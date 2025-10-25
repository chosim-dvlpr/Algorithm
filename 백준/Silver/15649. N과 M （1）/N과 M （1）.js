const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', (line) => {
  input.push(line.trim())
}).on('close', () => {
  const [n, m] = String(input).split(' ').map(Number)
  const arr = Array.from({ length: n }, (_, i) => i + 1)
  const result = []

  function recursion(ar, visited) {
    if (ar.length === m) {
      result.push(ar)
      return
    }
    for (let j = 0; j < n; j++) {
      if (!visited[j]) {
        visited[j] = true
        const newAr = [...ar, arr[j]]
        recursion(newAr, visited)
        visited[j] = false
      }
    }
  }

  for (let i = 0; i < n; i++) {
    const visited = Array(n).fill(false)
    visited[i] = true
    recursion([arr[i]], visited)
  }
  for (let r of result) {
    console.log(r.join(' '))
  }
})
