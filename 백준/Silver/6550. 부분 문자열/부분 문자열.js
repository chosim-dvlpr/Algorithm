const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', (line) => {
  input.push(line.trim())
}).on('close', () => {
  const strings = input.map(String)
  const result = []
  strings.forEach((str) => {
    const [s, t] = str.split(' ')
    let index = 0
    for (let i = 0; i < t.length; i++) {
      if (t[i] === s[index]) {
        index++
        if (index === s.length) {
          result.push('Yes')
          return
        }
      }
    }
    result.push('No')
  })
  console.log(result.join('\n'))
})
