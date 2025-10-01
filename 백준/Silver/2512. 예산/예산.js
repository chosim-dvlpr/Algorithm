const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on('line', (line) => {
  input.push(line.trim());
}).on('close', () => {
  // 모든 요청 가능 => 그대로 배정
  // 모든 요청 불가 => 상한액까지만 배정
  // 상한액을 어떻게 잡아야 모두가 만족할 것인가? & 최대로 줄 수 있는가?

  const [a, b, c] = input;
  const n = Number(a);
  const nums = b.split(' ').map(Number);
  const m = Number(c);

  const sums = nums.reduce((acc, curr) => acc + curr, 0);
  // 총합이 예산보다 많은 경우
  // 예산 => 평균을 상한으로 잡기 -> 예산보다 남으면 평균을 +1씩 ???

  if (sums > m) {
    let lim = Math.floor(m / n);
    let mx = 0;

    while (1) {
      let temp = 0;
      for (let num of nums) {
        temp += Math.min(num, lim);
      }
      if (temp <= m) {
        mx = Math.max(mx, temp);
        lim++;
      } else {
        lim--;
        break;
      }
    }
    console.log(lim);
  } else {
    console.log(Math.max(...nums));
  }
});
