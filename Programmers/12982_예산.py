def solution(d, budget):
    # d : 예산 리스트
    # budget : 가능한 최대 예산 (부족해도 됨)
    # 완전탐색
    
    d.sort()
    d_length = len(d)
    mx_cnt = 0 # 최대 부서 수
    
    for i in range(1, 1<<d_length):
        total = 0 # 비용 합계
        cnt = 0 # 지원 가능한 부서 수
        
        for j in range(d_length):
            if i & (1<<j): # i의 j번째 위치가 1이라면
                total += d[j]
                cnt += 1
                if total <= budget and mx_cnt < cnt:
                    mx_cnt = cnt

    return mx_cnt
