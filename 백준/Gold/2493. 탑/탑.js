const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on('line', (line) => {
  input.push(line.trim());
}).on('close', () => {
  const [a, b] = input;
  const n = Number(a);
  const arr = b.split(' ').map(Number);
  const result = Array.from({ length: n }, () => 0);
  const stack = [];
  for (let i = 0; i < arr.length; i++) {
    const h = arr[i];
    if (stack.length === 0) {
      stack.push([h, i]);
      continue;
    }
    while (stack.length > 0) {
      const last = stack.pop();
      if (last[0] >= h) {
        result[i] = last[1] + 1;
        stack.push(last);
        break;
      }
    }
    stack.push([h, i]);
  }
  console.log(result.join(' '));
});
