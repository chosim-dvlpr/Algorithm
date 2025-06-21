class MinHeap {
  constructor() {
    this.heap = [];
  }

  add(node, dist) {
    this.heap.push({ node, dist });
    this.bubbleUp();
  }
  pop() {
    const min = this.heap[0];
    const end = this.heap.pop();
    if (this.heap.length > 0) {
      this.heap[0] = end;
      this.bubbleDown();
    }
    return min;
  }
  swap(idx1, idx2) {
    [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]];
  }
  isEmpty() {
    return this.heap.length === 0;
  }
  bubbleUp() {
    let index = this.heap.length - 1;
    let parentIdx = Math.floor((index - 1) / 2);

    while (
      this.heap[parentIdx] &&
      this.heap[index].dist < this.heap[parentIdx].dist
    ) {
      this.swap(index, parentIdx);
      index = parentIdx;
      parentIdx = Math.floor((index - 1) / 2);
    }
  }
  bubbleDown() {
    let index = 0;

    while (index < this.heap.length) {
      let leftIdx = index * 2 + 1;
      let rightIdx = index * 2 + 2;
      let smallest = index;

      if (
        this.heap[leftIdx] &&
        this.heap[leftIdx].dist < this.heap[smallest].dist
      ) {
        smallest = leftIdx;
      }
      if (
        this.heap[rightIdx] &&
        this.heap[rightIdx].dist < this.heap[smallest].dist
      ) {
        smallest = rightIdx;
      }
      if (smallest === index) break;
      this.swap(smallest, index);
      index = smallest;
    }
  }
}

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on('line', (line) => {
  input.push(line.trim());
}).on('close', () => {
  const [n_m, ...input_arr] = input;
  const [n, m] = n_m.split(' ').map(Number);
  const arr = input_arr.map((a) => a.split(' ').map(Number));

  const graph = Array.from({ length: n + 1 }, () => []);
  arr.forEach(([s, e, cost]) => {
    graph[s].push([e, cost]);
    graph[e].push([s, cost]);
  });

  const INF = Infinity;
  const distance = Array(n + 1).fill(INF);

  function dijkstra(start) {
    const mh = new MinHeap();
    mh.add(start, 0);
    distance[start] = 0;

    while (!mh.isEmpty()) {
      const { node, dist } = mh.pop();
      if (distance[node] < dist) continue;

      for (let [adj, cost] of graph[node]) {
        const totalCost = distance[node] + cost;
        if (totalCost < distance[adj]) {
          distance[adj] = totalCost;
          mh.add(adj, totalCost);
        }
      }
    }
  }
  dijkstra(1);

  console.log(distance[n]);
});
