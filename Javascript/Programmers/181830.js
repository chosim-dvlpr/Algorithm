function solution(arr) {
    const answer = [[]];
    const zeroArr = []; // 0으로만 이루어진 배열
    for (i=0; i < arr.length; i++) {
        zeroArr.push(0);
    };
    
    for (i=0; i < arr.length; i++) {
        if (arr[i].length < arr.length) {
            
            arr[i].push(0)
        }
    }
    return answer;
}
