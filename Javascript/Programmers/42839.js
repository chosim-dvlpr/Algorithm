function solution(numbers) {
    
    function isPrime(number) { // 소수면 true
        if (number <= 1) {
            return false;
        }
        for (let i = 2; i <= Math.sqrt(number); i++) {
            if (number % i === 0) {
                return false;
            }
        }
        return true;
    }
    
    const arr = numbers.split('');
    const n = arr.length;
    let visited = new Array(n).fill(false);
    let temp = new Array(n).fill('');
    let tempSet = new Set();
    let result = 0;
    
    function dfs(depth, length) {
        if (depth === length) {
            const num = Number(temp.join(""));
            if (num > 0 && !tempSet.has(num) && isPrime(num)) {
                tempSet.add(num);
                result++;
            }
            return
        }
        for (let j=0; j < n; j++) {
            if (!visited[j]) {
                visited[j] = true
                temp[depth] = arr[j]
                dfs(depth+1, length);
                visited[j] = false
            }
        }
    }
    
    for (i=1; i <= n; i++) {
        dfs(0, i)
    }
    
    return result;
}
