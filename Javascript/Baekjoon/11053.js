const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on('line', (line) => {
  input.push(line.trim());
}).on('close', () => {
  const [x, ...inputArr] = input;
  const n = Number(x);
  const arr = inputArr[0].split(' ').map(Number);
  const dp = Array(n).fill(1);

  for (let i = 0; i < n - 1; i++) {
    for (let j = i + 1; j < n; j++) {
      if (arr[i] < arr[j]) {
        dp[j] = Math.max(dp[j], dp[i] + 1);
      }
    }
  }
  console.log(Math.max(...dp))
});
