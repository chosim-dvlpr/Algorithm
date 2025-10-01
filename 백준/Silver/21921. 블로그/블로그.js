const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on('line', (line) => {
  input.push(line.trim());
}).on('close', () => {
  // 0명 => SAD 출력
  // x일 동안 가장 많이 들어온 방문자 수 출력 후 둘째 줄에 기간 출력
  const [a, b] = input;
  const [n, x] = a.split(' ').map(Number);
  const nums = b.split(' ').map(Number);

  let mx = 0;
  let cnt = 1;

  for (let i = 0; i < x; i++) {
    mx += nums[i];
  }
  let temp = mx;

  for (let i = x; i < n; i++) {
    temp -= nums[i - x];
    temp += nums[i];

    if (mx < temp) {
      cnt = 1;
      mx = temp;
    } else if (mx === temp) {
      cnt++;
    }
  }
  console.log(mx === 0 ? 'SAD' : `${mx}\n${cnt}`);
});
