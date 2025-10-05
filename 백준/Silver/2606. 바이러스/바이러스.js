const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on('line', (line) => {
  input.push(line.trim());
}).on('close', () => {
  const [a, b, ...arr] = input;
  const n = Number(a);
  const graph = Array.from({ length: n + 1 }, () => []);
  const visited = Array(n + 1).fill(false);
  visited[1] = true;
  let cnt = 0;

  arr.forEach((ar) => {
    const [x, y] = ar.split(' ').map(Number);
    graph[x].push(y);
    graph[y].push(x);
  });

  function dfs(node) {
    for (let next of graph[node]) {
      if (!visited[next]) {
        visited[next] = true;
        cnt++;
        dfs(next);
      }
    }
  }
  dfs(1);
  console.log(cnt);
});
