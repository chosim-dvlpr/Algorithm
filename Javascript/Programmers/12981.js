function solution(n, words) {
    let answers = [];
    let prev = words[0][0];
    let i = 0;
    while (i !== words.length) {
        let cnt = parseInt(i/n)+1; // 개인이 단어를 외친 횟수
        let num = i%n+1; // 해당 인덱스의 사람의 번호
        if (words[i][0] !== prev || answers.includes(words[i])) {
            return [num, cnt]
        }
        prev = words[i].substr(-1);
        answers.push(words[i]);
        i++;
    }
    return [0, 0]
}
