const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on('line', (line) => {
  input.push(line.trim());
}).on('close', () => {
  // 1. 올바른 괄호가 아니면 0 출력
  // 2. 닫히는 괄호 찾기
  const arr = String(input);
  const stack = [];
  let result = 0;
  let temp = 0;
  let sums = 0;
  let flag = false;

  function calcStack() {
    let sums = 1;
    for (let i = stack.length - 1; i >= 0; i--) {
      if (stack[i] === '(') {
        sums *= 2;
      } else if (stack[i] === '[') {
        sums *= 3;
      }
    }
    return sums;
  }

  for (let i = 0; i < arr.length; i++) {
    const a = arr[i];
    // console.log('==========', a);
    if (a === '(') {
      stack.push(a);
    } else if (a === '[') {
      stack.push(a);
    } else if (a === ')') {
      if (arr[i - 1] === '(') {
        sums += calcStack();
      }
      const last = stack.pop();
      if (last !== '(') {
        temp = 0;
        flag = true;
        break;
      }
    } else if (a === ']') {
      if (arr[i - 1] === '[') {
        sums += calcStack();
      }
      const last = stack.pop();
      if (last !== '[') {
        temp = 0;
        flag = true;
        break;
      }
    }
    // console.log(sums);
    if (sums !== 0) {
      temp += sums;
    }
    sums = 0;
    // console.log('temp: ', temp);
    if (stack.length === 0 && temp !== 0) {
      result += temp;
      temp = 0;
      // console.log('result: ', result);
    }
  }
  console.log(flag ? 0 : result);
});
