class MinHeap {
  constructor() {
    this.heap = []
  }
  size() {
    return this.heap.length
  }
  isEmpty() {
    return this.heap.length === 0
  }
  swap(idx1, idx2) {
    ;[this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]]
  }
  add(value) {
    this.heap.push(value)
    this.bubbleUp()
  }
  getFirst() {
    return this.heap[0]
  }
  bubbleUp() {
    let index = this.size() - 1
    let parent = Math.floor((index - 1) / 2)

    while (this.heap[parent] && this.heap[index] < this.heap[parent]) {
      this.swap(index, parent)
      index = parent
      parent = Math.floor((index - 1) / 2)
    }
  }
  pop() {
    if (this.size() === 1) {
      return this.heap.pop()
    }
    const min = this.heap[0]
    const last = this.heap.pop()
    this.heap[0] = last

    this.bubbleDown()
    return min
  }
  bubbleDown() {
    let index = 0
    while (this.heap[index * 2 + 1]) {
      let left = index * 2 + 1
      let right = index * 2 + 2
      let smallest = left

      if (this.heap[right] && this.heap[left] > this.heap[right]) {
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
  const [a, ...b] = input
  const n = Number(a)
  const arr = b.map((ar) => ar.split(' ').map(Number))
  arr.sort((a, b) => a[0] - b[0] || a[1] - b[1])

  if (n === 1) {
    console.log(1)
    return
  }

  const mh = new MinHeap()
  const [_, e] = arr[0]
  mh.add(e)

  for (let i = 1; i < n; i++) {
    const [s, e] = arr[i]
    const end = mh.getFirst()

    if (s >= end) {
      mh.pop()
    }
    mh.add(e)
  }
  console.log(mh.size())
})
