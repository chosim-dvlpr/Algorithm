const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on('line', (line) => {
  input.push(line.trim());
}).on('close', () => {
  const n = String(input);
  let nI = 0;
  let curr = 1;
  while (nI < n.length) {
    const strCurr = String(curr);
    // 문자열 전체 비교
    if (strCurr === n.slice(nI, nI + strCurr.length)) {
      curr++;
      nI += strCurr.length;
      continue;
    }
    for (let i = 0; i < strCurr.length; i++) {
      if (strCurr[i] === n[nI]) {
        nI++;
      }
    }
    curr++;
  }
  console.log(curr - 1);
});
