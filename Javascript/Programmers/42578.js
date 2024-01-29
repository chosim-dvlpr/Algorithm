function solution(clothes) {
    let dict = {};
    clothes.forEach((c, i) => {
        if (dict[c[1]] !== undefined) {
            dict[c[1]] += 1
        } else {
            dict[c[1]] = 1
        }
    })
    
    const keys = Object.keys(dict);
    let answer = 1;
    keys.forEach((key, i) => {
        answer *= dict[key] + 1;
    })
    return answer - 1;
}
