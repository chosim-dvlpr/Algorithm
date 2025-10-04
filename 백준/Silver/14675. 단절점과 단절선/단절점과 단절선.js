const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on('line', (line) => {
  input.push(line.trim());
}).on('close', () => {
  // 단절선 => 항상 yes

  const [a, ...arr] = input;
  const n = Number(a); // 정점의 개수
  const graph = Array(n + 1).fill(0);

  for (let i = 0; i < n - 1; i++) {
    const [a, b] = arr[i].split(' ').map(Number);
    graph[a]++;
    graph[b]++;
  }

  const q = Number(arr[n - 1]);
  const result = [];
  for (let i = n; i < q + n; i++) {
    const [t, k] = arr[i].split(' ').map(Number);

    if (t === 2 || graph[k] > 1) {
      result.push('yes');
    } else {
      result.push('no');
    }
  }
  console.log(result.join('\n'));
});
