function solution(distance, rocks, n) {
    // 바위를 n개 제거한 뒤 각 지점 사이의 거리의 최솟값 중 가장 큰 값 반환하기
    let result = 0
    rocks.sort((a,b) => a - b)
    rocks.unshift(0)
    rocks.push(distance)

    let s=0
    let e=distance
    while (s<=e) {
        let mid = Math.floor((s+e)/2)
        let prev = 0
        let removed = 0
        for (let i=1; i < rocks.length;i++) {
            if (rocks[i]-rocks[prev]<mid) {
                removed++
            } else {
                prev = i
            }
        }
        if (removed > n) {
            e = mid-1
        } else {
            s = mid+1
            result = Math.max(result, mid)
        }
    }
    return result
}