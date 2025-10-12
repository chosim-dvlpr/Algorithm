const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', (line) => {
  input.push(line.trim())
}).on('close', () => {
  // X : 땅, . : 바다
  // 50년 후 => 인접한 세칸 이상 바다가 있는 땅은 잠겨버림
  // 50년 후 지도 => 지도 크기도 작아짐, 섬은 적어도 한 개, 지도 범위 벗어난 칸은 모두 바다
  const [a, ...b] = input
  const [r, c] = a.split(' ').map(Number)
  const arr = b.map((ar) => ['.', ...ar.split(''), '.'])
  arr.unshift(Array(c + 2).fill('.'))
  arr.push(Array(c + 2).fill('.'))

  const newArr = []
  arr.forEach((ar) => newArr.push(ar.slice()))

  function checkNearFloor(x, y) {
    const delta = [
      [0, 1],
      [1, 0],
      [-1, 0],
      [0, -1],
    ]
    let cnt = 0
    for (let [dx, dy] of delta) {
      const nx = x + dx,
        ny = y + dy
      if (
        0 <= nx &&
        nx < r + 2 &&
        0 <= ny &&
        ny < c + 2 &&
        arr[nx][ny] === '.'
      ) {
        // 주변 바다 확인
        cnt++
        if (cnt >= 3) {
          return true
        }
      }
    }
    return false
  }

  // 바다 잠김
  for (let i = 1; i < r + 1; i++) {
    for (let j = 1; j < c + 1; j++) {
      if (arr[i][j] === 'X') {
        // find 주변 칸
        if (checkNearFloor(i, j)) {
          newArr[i][j] = '.'
        }
      }
    }
  }
  const leftBottom = [0, 0]
  const rightTop = [0, 0]
  // 지도 축소
  // 가로 확인
  for (let i = 1; i < r + 1; i++) {
    const ar = newArr[i]
    if (!ar.every((a) => a === '.')) {
      leftBottom[0] = i
    }
  }
  for (let i = r; i > 0; i--) {
    const ar = newArr[i]
    if (!ar.every((a) => a === '.')) {
      // 땅을 보는경우
      rightTop[0] = i
    }
  }
  // 세로 확인
  for (let i = 1; i < c + 1; i++) {
    let flag = false
    for (let j = 1; j < r + 1; j++) {
      const ar = newArr[j][i]
      if (ar === 'X') {
        // 땅을 처음으로 보는 경우
        leftBottom[1] = i
        flag = true
        break
      }
    }
    if (flag) {
      break
    }
  }
  for (let i = c; i > 0; i--) {
    let flag = false
    for (let j = 0; j < r + 1; j++) {
      const ar = newArr[j][i]
      if (ar === 'X') {
        rightTop[1] = i
        flag = true
        break
      }
    }
    if (flag) {
      break
    }
  }

  const result = []
  for (let i = rightTop[0]; i < leftBottom[0] + 1; i++) {
    result.push(newArr[i].slice(leftBottom[1], rightTop[1] + 1))
  }
  console.log(result.map((r)=>r.join('')).join('\n'))
})
