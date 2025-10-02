const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on('line', (line) => {
  input.push(line.trim());
}).on('close', () => {
  const arr = String(input);
  let currStick = 0;
  let result = 0;
  let i = 0;
  while (i < arr.length) {
    // 레이저 확인
    if (i + 1 < arr.length && arr[i] === '(' && arr[i + 1] === ')') {
      result += currStick;
      i += 2;
      continue;
    }
    if (arr[i] === '(') {
      currStick++;
    } else if (arr[i] === ')') {
      currStick--;
      result++;
    }
    i++;
  }
  console.log(result);
});
