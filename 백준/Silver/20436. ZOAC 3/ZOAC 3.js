const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', (line) => {
  input.push(line.trim())
}).on('close', () => {
  // 자음 - 왼쪽 검지
  // 모음 - 오른쪽 검지
  // 이동하는데 걸린 시간 + 키를 누르는데 1초
  // 두 손 동시X
  // 걸리는 시간의 최솟값

  // 1 + 1 + 1 + 1+ 4
  const [a, word] = input
  const [l, r] = a.split(' ')

  const leftRange = [4, 4, 3]

  const keyboard = [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm'],
  ]

  const lStart = [0, 0]
  const rStart = [0, 0]
  let result = 0
  for (let i = 0; i < keyboard.length; i++) {
    for (let j = 0; j < keyboard[i].length; j++) {
      if (keyboard[i][j] === l) {
        lStart[0] = i
        lStart[1] = j
      } else if (keyboard[i][j] === r) {
        rStart[0] = i
        rStart[1] = j
      }
    }
  }

  function findWord(word) {
    for (let i = 0; i < keyboard.length; i++) {
      for (let j = 0; j < keyboard[i].length; j++) {
        if (keyboard[i][j] === word) {
          if (j <= leftRange[i]) {
            return [true, i, j]
          } else {
            return [false, i, j]
          }
        }
      }
    }
  }
  for (let w of word) {
    const [isLeft, i, j] = findWord(w)
    const start = [
      isLeft ? lStart[0] : rStart[0],
      isLeft ? lStart[1] : rStart[1],
    ]

    result += 1 + Math.abs(start[0] - i) + Math.abs(start[1] - j)

    if (isLeft) {
      lStart[0] = i
      lStart[1] = j
    } else {
      rStart[0] = i
      rStart[1] = j
    }
  }

  console.log(result)
})
