const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on('line', (line) => {
  input.push(line.trim());
}).on('close', () => {
  // 노드 제거 -> 하위 서브 트리 제거
  // 리프 노드 개수 구하기

  const [a, b, c] = input;
  const n = Number(a);
  const parents = b.split(' ').map(Number);
  const removeNode = Number(c);

  const graph = Array.from({ length: n }, () => []);
  let root = 0;
  parents.forEach((parent, index) => {
    if (parent === -1) {
      root = index;
      return;
    }
    graph[parent].push(index);
  });

  // 리프 노드 개수 세기
  let leaf = 0;
  function countLeaf(node) {
    if (graph[node].length === 0) {
      leaf++;
      return;
    }
    for (let next of graph[node]) {
      if (next === removeNode) continue;
      countLeaf(next);
    }
    if (graph[node].length === 1 && graph[node][0] === removeNode) {
      leaf++;
    }
  }

  // 서브 트리 제거
  graph[removeNode] = [];
  countLeaf(root);

  console.log(removeNode === root ? 0 : leaf);
});
