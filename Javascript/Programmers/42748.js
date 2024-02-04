function solution(array, commands) {
    let answer = [];
    commands.forEach((c) => {
        const newArray = [...array]
        const spliced = newArray.splice(c[0]-1, c[1]-c[0]+1);
        spliced.sort((a, b) => a - b);
        answer.push(spliced[c[2]-1])
    })
    return answer
}
