const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', (line) => {
  input.push(line.trim())
}).on('close', () => {
  // 같은 원소 카운팅 => 새로운 원소 들어오면 해당 개수와 mx값 비교
  //-> mx가 k보다 커진다면 왼쪽 인덱스 ++
  const [a, b] = input
  const [n, k] = a.split(' ').map(Number)
  const arr = b.split(' ').map(Number)
  const nums = new Map()
  let s = 0
  let e = 0
  let mx = 0 // 최장 길이

  while (s < n && e < n) {
    if (!nums.has(arr[e])) {
      nums.set(arr[e], 1)
      e++
      continue
    }
    // 오른쪽 증가하면서 중복값 확인
    nums.set(arr[e], nums.get(arr[e]) + 1)
    if (nums.get(arr[e]) > k) {
      mx = Math.max(mx, e - s)
      while (nums.get(arr[e]) > k && s < e) {
        nums.set(arr[s], nums.get(arr[s]) - 1)
        s++
      }
    }
    e++
  }
  mx = Math.max(mx, e - s)
  console.log(mx)
})
