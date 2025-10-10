class minHeap {
  constructor() {
    this.heap = []
  }
  swap(i, j) {
    ;[this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]]
  }
  size() {
    return this.heap.length
  }
  add(value) {
    this.heap.push(value) // [노드 번호, 비용]
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
      if (this.heap[right] && this.heap[right][1] < this.heap[left][1]) {
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
  // 1번과 N번 발전소를 잇는 값 중 최솟값 => 가중치, 음수X => 다익스트라
  const [a, b, ...c] = input
  const [n, w] = a.split(' ').map(Number) // 발전소의 수, 현재 남아있는 전선의 수
  const m = parseFloat(b) // 추가로 설치하는 전선의 길이의 최댓값
  const edges = []
  const connections = Array.from({ length: n + 1 }, () => [])
  const costs = Array(n + 1).fill(Infinity)

  for (let i = 0; i < n; i++) {
    edges.push(c[i].split(' ').map(Number))
  }

  for (let i = n; i < n + w; i++) {
    const [a, b] = c[i].split(' ').map(Number)
    connections[a].push([b, 0])
    connections[b].push([a, 0])
  }

  for (let i = 1; i < n + 1; i++) {
    for (let j = 1; j < n + 1; j++) {
      if (i === j) continue
      // i에서 j까지의 길이
      const [x1, y1] = edges[i - 1]
      const [x2, y2] = edges[j - 1]
      const dist = Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
      if (dist <= m) {
        connections[i].push([j, dist])
        connections[j].push([i, dist])
      }
    }
  }

  const mh = new minHeap()
  mh.add([1, 0])
  costs[1] = 0

  while (mh.size() > 0) {
    const [curr, currCost] = mh.pop()

    if (costs[curr] < currCost) continue

    for (let [next, cost] of connections[curr]) {
      const newCost = cost + costs[curr]
      if (newCost < costs[next]) {
        costs[next] = newCost
        mh.add([next, newCost])
      }
    }
  }
  console.log(Math.floor(costs[n] * 1000))
})
