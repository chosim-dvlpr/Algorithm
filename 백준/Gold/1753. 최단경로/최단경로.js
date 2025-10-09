class minHeap {
  constructor() {
    this.heap = []
  }
  size() {
    return this.heap.length
  }
  swap(i, j) {
    ;[this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]]
  }
  add(value) {
    this.heap.push(value)
    this.bubbleUp()
  }
  pop() {
    if (this.size() === 1) {
      return this.heap.pop()
    }
    const min = this.heap[0]
    this.heap[0] = this.heap.pop()
    this.bubbleDown()
    return min
  }
  bubbleUp() {
    let index = this.size() - 1
    let parent = Math.floor((index - 1) / 2)
    while (this.heap[parent] && this.heap[parent][1] > this.heap[index][1]) {
      this.swap(index, parent)
      index = parent
      parent = Math.floor((index - 1) / 2)
    }
  }
  bubbleDown() {
    let index = 0
    while (index * 2 + 1 < this.size()) {
      let left = index * 2 + 1
      let right = index * 2 + 2
      let smallest = left
      if (this.heap[right] && this.heap[left][1] > this.heap[right][1]) {
        smallest = right
      }
      if (this.heap[index][1] <= this.heap[smallest][1]) {
        break
      }
      this.swap(index, smallest)
      index = smallest
    }
  }
}

const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', (line) => {
  input.push(line.trim())
}).on('close', () => {
  const [a, b, ...c] = input
  const [v, e] = a.split(' ').map(Number)
  const start = Number(b)

  const graph = Array.from({ length: v + 1 }, () => [])
  const costs = Array(v + 1).fill(Infinity)
  costs[start] = 0

  c.forEach((ar) => {
    const [a, b, c] = ar.split(' ').map(Number)
    graph[a].push([b, c])
  })

  const mh = new minHeap()
  mh.add([start, 0])

  while (mh.size() > 0) {
    const [curr, currDist] = mh.pop()
    if (costs[curr] < currDist) continue

    for (let [next, cost] of graph[curr]) {
      const newCost = cost + currDist
      if (costs[next] > newCost) {
        costs[next] = newCost
        mh.add([next, newCost])
      }
    }
  }
  const result = []
  for (let i = 1; i < costs.length; i++) {
    const c = costs[i]
    if (c === Infinity) {
      result.push('INF')
    } else {
      result.push(c)
    }
  }
  console.log(result.join('\n'))
})
