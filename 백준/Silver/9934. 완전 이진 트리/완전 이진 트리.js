const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on('line', (line) => {
  input.push(line.trim());
}).on('close', () => {
  // 왼 - 루트 - 오
  // 각 레벨에 있는 빌딩의 번호를 구하기
  // 방문 순서를 먼저 아는 경우 트리를 구하기
  // 완전 이진 트리 - 마지막 레벨의 노드를 제외하고 모든 노드가 채워져 있음, 왼쪽에서 오른쪽 방향으로 채워짐
  const [a, b] = input;
  const k = Number(a);
  const n = 2 ** k - 1;
  const order = b.split(' ').map(Number);
  const rootIndex = Math.floor(n / 2);
  const root = order[rootIndex];
  const graph = Array.from({ length: n + 1 }, () => []);
  const result = Array.from({ length: k + 1 }, () => []);

  function binary(array, root) {
    // 마지막 노드에 다다른 경우
    if (array.length === 1) {
      const child = order.pop();
      graph[root].unshift(child);
      return;
    }

    const nextRootIndex = Math.floor(array.length / 2);
    const nextRoot = array[nextRootIndex];
    const right = array.slice(nextRootIndex + 1, array.length);
    const left = array.slice(0, nextRootIndex);
    binary(right, nextRoot);
    const child = order.pop();
    if (child !== root) {
      graph[root].unshift(child);
    }
    binary(left, nextRoot);
  }
  binary(order, order[rootIndex]);

  function getTree(depth, node) {
    if (depth > k) return;
    result[depth].push(node);

    for (let n of graph[node]) {
      getTree(depth + 1, n);
    }
  }

  getTree(1, root);

  for (let i = 1; i < k + 1; i++) {
    console.log(result[i].join(' '));
  }
});
