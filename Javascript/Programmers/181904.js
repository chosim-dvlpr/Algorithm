function solution(my_string, m, c) {
  var lst = [];
  for (i=0; i < my_string.length; i++) {
    if (i < m) {
      lst.push(my_string[i])
    } else {
      var idx = i % m;
      lst[idx] = lst[idx] + my_string[i];
    }    
  }
  var answer = lst[c-1];
  return answer;
}