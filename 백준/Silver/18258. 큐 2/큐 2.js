const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on('line', (line) => {
  input.push(line.trim());
}).on('close', () => {
  const [_, ...arr] = input;
  const q = [];
  const result = [];
  let i = 0;

  for (let a of arr) {
    const command = a.split(' ');
    const com = command[0];
    if (com === 'push') {
      q.push(command[1]);
    } else if (com === 'pop') {
      result.push(i < q.length ? q[i] : -1);
      if (i < q.length) i++;
    } else if (com === 'size') {
      result.push(q.length - i);
    } else if (com === 'empty') {
      result.push(i >= q.length ? 1 : 0);
    } else if (com === 'front') {
      result.push(i >= q.length ? -1 : q[i]);
    } else if (com === 'back') {
      result.push(i >= q.length ? -1 : q.at(-1));
    }
  }
  console.log(result.join('\n'));
});
