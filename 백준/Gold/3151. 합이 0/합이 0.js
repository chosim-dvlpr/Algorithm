const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', (line) => {
  input.push(line.trim())
}).on('close', () => {
  const [a, b] = input
  const n = Number(a)
  const arr = b.split(' ').map(Number)
  let result = 0n
  if (n < 3) {
    console.log(result.toString())
    return
  }
  arr.sort((a, b) => a - b) // 오름차순 정렬
  for (let i = 0; i < n - 2; i++) {
    const target = -BigInt(arr[i])
    let j = i + 1
    let k = n - 1
    while (j < k) {
      const sums = BigInt(arr[j]) + BigInt(arr[k])

      if (sums > target) {
        k--
      } else if (sums < target) {
        j++
      } else {
        if (arr[j] === arr[k]) {
          const count = BigInt(k - j + 1)
          result += (count * (count - 1n)) / 2n
          break
        } else {
          let jCount = 0n
          let kCount = 0n
          const jVal = arr[j]
          const kVal = arr[k]

          while (j < k && arr[j] === jVal) {
            j++
            jCount++
          }
          while (k >= j && arr[k] === kVal) {
            k--
            kCount++
          }

          result += jCount * kCount
        }
      }
    }
  }

  console.log(result.toString())
})
