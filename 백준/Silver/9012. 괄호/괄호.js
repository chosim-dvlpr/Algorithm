const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on('line', (line) => {
  input.push(line.trim());
}).on('close', () => {
  const [b, ...arr] = input;
  const n = Number(b);
  const result = [];

  for (let ar of arr) {
    const stack = [];
    let flag = false;
    for (let a of ar) {
      if (a === '(') {
        stack.push(a);
      } else {
        if (stack.length === 0) {
          result.push('NO');
          flag = true;
          break;
        } else {
          stack.pop();
        }
      }
    }
    if (!flag) {
      if (stack.length > 0) {
        result.push('NO');
      } else {
        result.push('YES');
      }
    }
  }
  console.log(result.join('\n'));
});
