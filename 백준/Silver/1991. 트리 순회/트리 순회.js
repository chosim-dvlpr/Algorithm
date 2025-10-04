const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on('line', (line) => {
  input.push(line.trim());
}).on('close', () => {
  const [a, ...ar] = input;
  const n = Number(a);
  const graph = Array.from({ length: n + 1 }, () => []);

  for (let a of ar) {
    const root = a.charCodeAt(0) - 64;
    const left = a.charCodeAt(2) - 64;
    const right = a.charCodeAt(4) - 64;

    graph[root].push(left === -18 ? 0 : left);
    graph[root].push(right === -18 ? 0 : right);
  }

  // 전위순회: 루트 - 왼 - 오
  let pre = '';
  function preOrder(index) {
    const next = graph[index];
    pre += String.fromCharCode(index + 64); // 루트
    if (next[0] !== 0) {
      preOrder(next[0]); // 왼
    }
    if (next[1] !== 0) {
      preOrder(next[1]); // 오
    }
  }
  preOrder(1);

  // 중위순회
  let inO = '';
  function inOrder(index) {
    const next = graph[index];
    if (next[0] !== 0) {
      inOrder(next[0]); // 왼
    }
    inO += String.fromCharCode(index + 64); // 루트
    if (next[1] !== 0) {
      inOrder(next[1]); // 오
    }
  }
  inOrder(1);

  // 후위순회
  let postO = '';
  function postOrder(index) {
    const next = graph[index];
    if (next[0] !== 0) {
      postOrder(next[0]); // 왼
    }
    if (next[1] !== 0) {
      postOrder(next[1]); // 오
    }
    postO += String.fromCharCode(index + 64); // 루트
  }
  postOrder(1);

  console.log(pre);
  console.log(inO);
  console.log(postO);
});
