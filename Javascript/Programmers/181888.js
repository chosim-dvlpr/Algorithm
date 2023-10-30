function solution(num_list, n) {
    var answer = [];
    for (i=0; i<(num_list.length); i++) {
        if (n*i < num_list.length) {
            answer.push(num_list[n*i]);
        }
    }
    return answer;
}
