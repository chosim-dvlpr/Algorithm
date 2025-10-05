const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on('line', (line) => {
  input.push(line.trim());
}).on('close', () => {
  // 특정 노드부터 다른 노드까지의 가장 긴 거리 구하기
  // 재귀
  const [a, ...arr] = input;
  const n = Number(a);
  if (n === 1) {
    console.log(0);
    return;
  }
  const graph = Array.from({ length: n + 1 }, () => []);

  arr.forEach((ar) => {
    const [a, b, cost] = ar.split(' ').map(Number);
    graph[a].push([b, cost]);
    graph[b].push([a, cost]);
  });

  const visited = Array(n + 1).fill(false);
  let lastNode = 0;
  let lastNodeMax = 0;
  function dfs(node, sums) {
    if (graph[node].length <= 1 && sums > lastNodeMax) {
      lastNode = node;
      lastNodeMax = sums;
      return;
    }

    for (let [next, cost] of graph[node]) {
      if (!visited[next]) {
        visited[next] = true;
        dfs(next, sums + cost);
      }
    }
  }
  visited[1] = true;
  dfs(1, 0);
  if (n === 2) {
    console.log(lastNodeMax);
    return;
  }
  for (let i = 0; i < n + 1; i++) {
    visited[i] = false;
  }
  visited[lastNode] = true;
  dfs(lastNode, 0);
  console.log(lastNodeMax);
});
