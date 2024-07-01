function solution(n, k) {
    let nums = Array.from({length: n}, (_, index) => index+1)
    let res = []
    
    function fac(n) {
        if (n <= 1) return 1
        return n * fac(n-1)
    }
    
    k--
    while (1) {
        if (k === 0) {
            res.push(...nums)
            break
        }
        n--
        const index = Math.floor(k / fac(n))
        
        res.push(nums[index])
        k %= fac(n)
        
        nums.splice(index, 1)
    }
    return res
}
