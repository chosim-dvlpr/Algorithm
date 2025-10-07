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
  getFirst() {
    return this.heap[0]
  }
  add(value) {
    this.heap.push(value)
    this.bubbleUp()
  }
  pop() {
    if (this.heap.length === 1) {
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
    while (this.heap[parent] && this.heap[parent] > this.heap[index]) {
      this.swap(index, parent)
      index = parent
      parent = Math.floor((index - 1) / 2)
    }
  }
  bubbleDown() {
    let index = 0
    while (this.heap[index * 2 + 1]) {
      let left = index * 2 + 1
      let right = index * 2 + 2
      let smallest = left
      if (this.heap[right] && this.heap[right] < this.heap[left]) {
        smallest = right
      }
      if (this.heap[index] <= this.heap[smallest]) {
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
  const [a, ...arr] = input
  const n = Number(a)
  const meetings = arr.map((ar) => ar.split(' ').map(Number))
  meetings.sort((a, b) => a[0] - b[0] || a[1] - b[1])
  const mh = new minHeap()
  mh.add(meetings[0][1])

  for (let i = 1; i < n; i++) {
    const [s, e] = meetings[i]
    const end = mh.getFirst()
    if (s >= end) {
      mh.pop()
    }
    mh.add(e)
  }
  console.log(mh.size())
})
