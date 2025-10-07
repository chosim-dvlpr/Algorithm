const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', (line) => {
  input.push(line.trim())
}).on('close', () => {
  const [a, ...arr] = input
  const n = Number(a)
  const meetings = arr.map((ar) => ar.split(' ').map(Number))
  meetings.sort((a, b) => a[1] - b[1] || a[0] - b[0])
  let lastMeetingEnd = 0
  let cnt = 0
  for (let [s, e] of meetings) {
    if (lastMeetingEnd <= s) {
      lastMeetingEnd = e
      cnt++
    }
  }
  console.log(cnt)
})
