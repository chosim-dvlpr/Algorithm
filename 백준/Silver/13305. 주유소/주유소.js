const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on('line', (line) => {
  input.push(line.trim());
}).on('close', () => {
  const [inputN, inputRoads, inputPrices] = input;
  const n = Number(inputN);
  const roads = inputRoads.split(' ').map(BigInt);
  const prices = inputPrices.split(' ').map(BigInt);
  let mn = BigInt(prices[0]);
  let sums = BigInt(0);
  for (let i = 0; i < n - 1; i++) {
    if (prices[i] < mn) {
      mn = prices[i];
    }
    sums += mn * roads[i];
  }
  console.log(sums.toString());
});
