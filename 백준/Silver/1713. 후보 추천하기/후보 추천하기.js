const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', (line) => {
  input.push(line.trim())
}).on('close', () => {
  // map
  // 20*1000?
  const [a, b, d] = input
  const n = Number(a)
  const m = Number(b)
  const arr = d.split(' ').map(Number)
  const c = new Map()
  const INF = Infinity

  function findTarget() {
    let mnCnt = INF
    let mnTime = INF
    let targetStd = -1
    for (let [stdId, [cnt, time]] of c.entries()) {
      if (cnt < mnCnt) {
        mnCnt = cnt
        mnTime = time
        targetStd = stdId
      } else if (cnt === mnCnt) {
        if (time < mnTime) {
          mnTime = time
          targetStd = stdId
        }
      }
    }
    return targetStd
  }

  for (let i = 0; i < m; i++) {
    const ar = arr[i]
    if (c.has(ar)) {
      c.set(ar, [c.get(ar)[0] + 1, c.get(ar)[1]])
    } else if (c.size === n) {
      // 모든 학생 순회 후 최솟값 & i가 더 작은 학생 찾기
      const target = findTarget()
      c.delete(target)
      c.set(ar, [1, i])
    } else {
      c.set(ar, [1, i])
    }
  }
  const result = [...c.keys()]
  result.sort((a, b) => a - b)
  console.log(result.join(' '))
})
