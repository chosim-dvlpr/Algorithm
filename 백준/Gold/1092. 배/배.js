const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', (line) => {
  input.push(line.trim())
}).on('close', () => {
  const [a, b, c, d] = input
  const n = Number(a)
  const cranes = b.split(' ').map(Number)
  const m = Number(c)
  const boxes = d.split(' ').map(Number)

  cranes.sort((a, b) => b - a)
  boxes.sort((a, b) => b - a)

  if (boxes[0] > cranes[0]) {
    console.log(-1)
    return
  }

  let second = 0
  const visited = Array(m).fill(false)
  let cnt = 0

  // let i = 0

  while (cnt < m) {
    second++
    let boxIndex = 0

    for (let i = 0; i < n; i++) {
      const crane = cranes[i]
      while (boxIndex < m) {
        if (visited[boxIndex]) {
          boxIndex++
          continue
        }
        const box = boxes[boxIndex]
        if (crane >= box) {
          visited[boxIndex] = true
          cnt++
          break
        } else {
          boxIndex++
        }
      }
    }
  }

  console.log(second)
})
