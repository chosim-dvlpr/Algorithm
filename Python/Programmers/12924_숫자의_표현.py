def solution(n):
    answer = 1 # 자기 자신만을 더한 값 추가
    i = 0
    
    while i < n:
        i += 1
        sums = 0
        for k in range(i, n):
            sums += k
            if sums == n:
                answer += 1
                break
            elif sums > n:
                break
    return answer
