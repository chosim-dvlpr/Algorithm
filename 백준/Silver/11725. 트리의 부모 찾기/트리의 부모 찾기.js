const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on('line', (line) => {
  input.push(line.trim());
}).on('close', () => {
  const [a, ...b] = input;
  const n = Number(a);
  const graph = Array.from({ length: n + 1 }, () => []);
  const result = Array(n + 1).fill(0);

  b.forEach((i) => {
    const [x, y] = i.split(' ').map(Number);
    graph[x].push(y);
    graph[y].push(x);
  });
  // console.log('graph : ', graph);

  function recursion(index, parent) {
    for (let g of graph[index]) {
      if (g !== parent) {
        result[g] = index;
        recursion(g, index);
      }
    }
  }
  recursion(1, 0);

  console.log(result.slice(2, n + 2).join('\n'));
});
