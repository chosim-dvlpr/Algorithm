const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on('line', (line) => {
  input.push(line.trim());
}).on('close', () => {
  class MinHeap {
    constructor() {
      this.heap = [];
    }
    insert(value) {
      this.heap.push(value);
      this.bubbleUp();
    }
    pop() {
      const min = this.heap[0];
      const end = this.heap.pop();
      if (this.heap.length === 0) {
        return end;
      }
      this.heap[0] = end;
      this.bubbleDown();
      return min;
    }
    swap(idx1, idx2) {
      [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]];
    }
    bubbleUp() {
      let index = this.heap.length - 1;
      let parentIdx = Math.floor((index - 1) / 2);

      while (
        this.heap.parentIdx &&
        this.heap[parentIdx][0] > this.heap[index][0]
      ) {
        this.swap(parentIdx, index);
        index = parentIdx;
        parentIdx = Math.floor((index - 1) / 2);
      }
    }
    bubbleDown() {
      let index = 0;
      while (index < this.heap.length) {
        let left = index * 2 + 1;
        let right = index * 2 + 2;
        let smallest = index;
        if (this.heap[left] && this.heap[left][0] < this.heap[index][0]) {
          smallest = left;
        }
        if (this.heap[right] && this.heap[right][0] < this.heap[index][0]) {
          smallest = right;
        }
        if (smallest === index) {
          break;
        }
        this.swap(smallest, index);
        index = smallest;
      }
    }
    isEmpty() {
      return this.heap.length === 0;
    }
  }

  const [inputN, inputM, ...inputArr] = input;
  const n = Number(inputN);
  const m = Number(inputM);
  const [start, end] = inputArr.pop().split(' ').map(Number);
  const graph = Array.from({ length: n + 1 }, () => []);
  let mn = Infinity;

  inputArr.forEach((arr) => {
    const [s, e, c] = arr.split(' ').map(Number);
    graph[s].push([e, c]);
  });

  function dijkstra(start) {
    const minHeap = new MinHeap();
    minHeap.insert([0, start]);
    const dist = Array(n + 1).fill(Infinity);
    dist[start] = 0;

    // while문으로 minHeap 반복
    while (!minHeap.isEmpty()) {
      const [currCost, curr] = minHeap.pop();

      // if (curr === end) break; 이미 방문한 지점이어도 다시 방문했을 때 더 가까울 수 있으므로 이 줄은 지워야 함
      if (currCost > dist[curr]) continue;
      for (let [next, cost] of graph[curr]) {
        const newCost = cost + currCost;
        if (newCost < dist[next]) {
          // 등호는 빼야 함
          dist[next] = newCost;
          minHeap.insert([newCost, next]);
        }
      }
    }
    mn = dist[end];
  }

  dijkstra(start);
  console.log(mn);
});
