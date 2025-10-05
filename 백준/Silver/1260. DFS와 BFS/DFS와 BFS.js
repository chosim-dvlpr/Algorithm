const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', (line) => {
  input.push(line.trim())
}).on('close', () => {
  const [a, ...inputArr] = input
  const [n, m, v] = a.split(' ').map(Number)
  const graph = Array.from({ length: n + 1 }, () => [])
  const arr = inputArr.map((k) => k.split(' ').map(Number))

  arr.forEach(([x, y]) => {
    graph[x].push(y)
    graph[y].push(x)
    graph[x].sort((a, b) => a - b)
    graph[y].sort((a, b) => a - b)
  })

  const dfsResult = []
  const bfsResult = [v]
  const visited = Array(n + 1).fill(false)
  visited[v] = true
  function dfs(node) {
    dfsResult.push(node)

    for (let next of graph[node]) {
      if (!visited[next]) {
        visited[next] = true
        dfs(next)
      }
    }
  }

  function bfs(start) {
    const q = [start]
    const visited = Array(n + 1).fill(false)
    visited[v] = true

    while (q.length > 0) {
      const node = q.shift()

      if (graph[node].length === 0) continue
      for (let next of graph[node]) {
        if (!visited[next]) {
          visited[next] = true
          bfsResult.push(next)
          q.push(next)
        }
      }
    }
  }

  dfs(v)
  bfs(v)

  console.log(dfsResult.join(' '))
  console.log(bfsResult.join(' '))
})
