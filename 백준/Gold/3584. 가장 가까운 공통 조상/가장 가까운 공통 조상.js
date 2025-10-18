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
  const tc = Number(a)

  for (let t = 0; t < tc; t++) {
    const n = Number(b.shift())
    const graph = Array.from({ length: n + 1 }, () => [])

    for (let i = 0; i < n - 1; i++) {
      const [x, y] = b.shift().split(' ').map(Number)
      graph[y].push(x)
    }

    const [tx, ty] = b.shift().split(' ').map(Number)
    const parents = new Map()

    // tx의 부모 노드 저장
    function recursion(node) {
      parents.set(node, true)

      if (graph[node].length === 0) {
        return
      }
      for (let next of graph[node]) {
        recursion(next)
      }
    }
    recursion(tx)

    // ty의 부모 노드 확인하면서 tx에 있는지 확인 => 있다면 종료
    let result = 0
    function checkParents(node) {
      if (parents.has(node)) {
        result = node
        return
      }

      if (graph[node].length === 0) {
        return
      }

      for (let next of graph[node]) {
        checkParents(next)
      }
    }
    checkParents(ty)
    console.log(result)
  }
})
