function solution(cap, n, deliveries, pickups) {
    // n-1 부터 왕복
    let answer = 0
    let d_todo = 0
    let p_todo = 0
    let i = n-1
    
    while (i>=0) {
        d_todo += deliveries[i]
        p_todo += pickups[i]
        
        while (d_todo > 0 || p_todo > 0) {
            answer += (i+1)*2
            d_todo -= cap
            p_todo -= cap
        }        
        i--      
    }
    return answer
}