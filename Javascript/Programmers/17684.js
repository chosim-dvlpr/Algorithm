function solution(msg) {
    // 문자 1개 - 출력
    // 문자 2개 이상
    // 1. 사전에 있는지 확인
    // 2-1. 있다면 -> 인덱스 출력 -> 다음 글자 확인
    // 2-2. 없다면 -> 사전에 등록
    // 문자열은 계속 늘어나는 형태
    // 다음 글자 확인 필요
    const result = [];
    
    const wordMap = new Map();
    for (let i=0; i < 26; i++) {
        const key = String.fromCharCode(i+65)
        const value = i+1
        wordMap.set(key, value)
    }
    let wordLength = 1;
    let i = 0;
    while (i < msg.length) {
        // 현재 문자열 + 다음 문자가 사전에 없을 때까지 반복
        let wordLength = 1;
        let curr = ''
        while (true) {
            curr += msg[i+wordLength-1]
            const next = msg[i+wordLength]

            if (next === undefined) {
                result.push(wordMap.get(curr))
                i += wordLength
                break
            }
            
            const newWord = curr + next
            const isGettingWord = wordMap.get(newWord)
            const mapLength = [...wordMap.keys()].length 
            
            if (!isGettingWord) { // 새로운 단어일 때
                wordMap.set(newWord, mapLength+1)
                result.push(wordMap.get(curr))
                i += wordLength
                break
            } else { // 존재하는 단어일 때
                wordLength++;
            } 
        }
    }
    
    return result;
    
}
