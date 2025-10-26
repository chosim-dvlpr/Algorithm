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
  function recur(s, visited, arr) {
    if (arr.length === m) {
      console.log(arr.join(' '))
      return
    }

    for (let i = s; i < n + 1; i++) {
      if (!visited[i]) {
        visited[i] = true
        recur(i, visited, [...arr, i])
        visited[i] = false
      }
    }
  }

  for (let i = 1; i < n + 1; i++) {
    const visited = Array(n + 1).fill(false)
    visited[i] = true
    recur(i, visited, [i])
  }
})
