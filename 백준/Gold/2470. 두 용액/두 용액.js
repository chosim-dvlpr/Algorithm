const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', (line) => {
  input.push(line.trim())
}).on('close', () => {
  // 서로 다른 값을 합해 0에 가장 가까운 값 만들기
  // 오름차순 정렬
  // 양끝값 -> 0보다 크면 오른쪽을 -1, 0보다 작으면 왼쪽을 +1
  const [a, b] = input
  const n = Number(a)
  const arr = b.split(' ').map(Number)
  arr.sort((a, b) => a - b)
  let diff = Infinity
  const result = [0, 0]
  let l = 0
  let r = n - 1

  while (l < r) {
    const sums = arr[l] + arr[r]
    if (sums > 0) {
      const d = Math.abs(0 - sums)
      if (diff > d) {
        diff = d
        result[0] = arr[l]
        result[1] = arr[r]
      }
      r--
    } else if (sums < 0) {
      const d = Math.abs(0 - sums)
      if (diff > d) {
        diff = d
        result[0] = arr[l]
        result[1] = arr[r]
      }
      l++
    } else {
      result[0] = arr[l]
      result[1] = arr[r]
      break
    }
  }

  console.log(result.join(' '))
})
