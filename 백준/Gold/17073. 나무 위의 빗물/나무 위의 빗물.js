const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on('line', (line) => {
  input.push(line.trim());
}).on('close', () => {
  // 자식 중 1개에 물 1 보내줌
  // 각 정점에 있는 물의 양의 평균 (0 제외)
  const [a, ...arr] = input;
  const [n, w] = a.split(' ').map(Number);
  const graph = Array.from({ length: n + 1 }, () => []);

  arr.forEach((ar) => {
    const [a, b] = ar.split(' ').map(Number);
    graph[a].push(b);
    graph[b].push(a);
  });

  const visited = Array(n + 1).fill(false);
  let cnt = 0;
  // 리프 노드라면 물의 양 계산
  function findLeaf(depth, node) {
    if (node !== 1 && graph[node].length === 1) {
      // console.log(node, depth, Math.floor(w / 2 ** (depth - 1)));
      cnt += 1;
      return;
    }

    for (let next of graph[node]) {
      if (!visited[next]) {
        visited[next] = true;
        findLeaf(depth + 1, next);
      }
    }
  }
  findLeaf(1, 1);
  console.log(w / cnt);
});
