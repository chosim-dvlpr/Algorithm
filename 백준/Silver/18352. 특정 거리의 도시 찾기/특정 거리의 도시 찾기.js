class minHeap {
  constructor() {
    this.heap = []
  }
  size() {
    return this.heap.length
  }
  swap(i1, i2) {
    ;[this.heap[i1], this.heap[i2]] = [this.heap[i2], this.heap[i1]]
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
    while (this.heap[parent] && this.heap[index][1] < this.heap[parent][1]) {
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
  const [a, ...b] = input
  const [n, m, k, x] = a.split(' ').map(Number)
  const graph = Array.from({ length: n + 1 }, () => [])
  b.forEach((ar) => {
    const [a, b] = ar.split(' ').map(Number)
    graph[a].push(b)
  })
  // 정확히 K가 되어야 함
  // 거리 = 1
  const DIST = 1
  const result = []
  const distances = Array(n + 1).fill(Infinity)
  distances[x] = 0
  const mh = new minHeap()
  mh.add([x, 0]) // 출발 도시, 거리

  while (mh.size() > 0) {
    const [curr, currDist] = mh.pop()
    if (distances[curr] < currDist) continue

    if (distances[curr] === k) {
      result.push(curr)
      continue
    }
    if (distances[curr] > k) {
      break
    }

    for (let next of graph[curr]) {
      const newDist = currDist + DIST
      if (newDist < distances[next]) {
        distances[next] = newDist
        mh.add([next, newDist])
      }
    }
  }
  result.sort((a, b) => a - b)
  console.log(result.length === 0 ? -1 : result.join('\n'))
})
