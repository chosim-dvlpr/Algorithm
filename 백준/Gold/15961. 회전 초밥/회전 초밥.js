const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', (line) => {
  input.push(line.trim())
}).on('close', () => {
  const [a, ...b] = input
  const [n, d, k, c] = a.split(' ').map(Number)
  const arr = b.map(Number)

  let mx = 0
  const nums = new Map()

  let temp = 0
  for (let s = 0; s < k; s++) {
    if (!nums.has(arr[s])) {
      temp++
    }
    nums.set(arr[s], (nums.get(arr[s]) || 0) + 1)
  }
  if (!nums.has(c)) {
    temp++
  }
  mx = temp
  let cnt = temp

  for (let start = k; start < n + k; start++) {
    const s = start % n
    if (nums.get(arr[(start - k) % n]) === 1) {
      nums.delete(arr[(start - k) % n])
    } else {
      nums.set(arr[(start - k) % n], nums.get(arr[(start - k) % n]) - 1)
    }
    nums.set(arr[s], (nums.get(arr[s]) || 0) + 1)
    cnt = nums.size
    if (!nums.has(c)) {
      cnt++
    }
    mx = Math.max(cnt, mx)
  }

  console.log(mx)
})
