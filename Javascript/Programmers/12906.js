function solution(arr) {

    // 다른 풀이
    return arr.filter((a, i) => a !== arr[i-1])
    
    // let prev = -1;
    // let answer = [];
    // arr.forEach((a, i) => {
    //     if (prev !== a) {
    //         answer.push(a)
    //     }
    //     prev = a
    // })
    // return answer;
}
