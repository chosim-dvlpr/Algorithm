function solution(word) {
    const words = ['A', 'E', 'I', 'O', 'U'];
    const arr = [];
    function dfs(str, depth) {
        if (depth > 5) return
        arr.push(str)
        for (let i=0; i < words.length; i++) {
            dfs(str+words[i], depth+1)
        }
    }
    dfs('', 0)
    const result = arr.indexOf(word)
    
    return result
}
