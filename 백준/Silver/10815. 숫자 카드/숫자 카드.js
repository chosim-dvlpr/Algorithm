const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', (line) => {
  input.push(line.trim())
}).on('close', () => {
  // 숫자카드 n개 중 m의 원소가 적혀있는 숫자를 갖고 있는지 구하기
  const [a, b, c, d] = input
  const n = Number(a)
  const cards = b.split(' ').map(Number)
  const m = Number(c)
  const numbers = d.split(' ').map(Number) // 순서 중요

  const cardNums = Array(20000000).fill(0)

  for (let card of cards) {
    cardNums[card] = 1
  }

  const result = []

  function binarySearch(start, end, num) {
    let s = start
    let e = end
    let mid = Math.floor((s + e) / 2)

    while (s <= e) {
      if (cardNums[mid] === 1 && mid === num) {
        return 1
      }
      if (mid < num) {
        s = mid + 1
      } else {
        e = mid - 1
      }
      mid = Math.floor((s + e) / 2)
    }
    return 0
  }

  for (let num of numbers) {
    // 5 * 10**5
    result.push(binarySearch(-10000000, 10000000, num))
  }

  console.log(result.join(' '))
})
