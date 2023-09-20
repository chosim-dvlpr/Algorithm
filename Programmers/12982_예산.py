def solution(d, budget):
    # d : 예산 리스트
    # budget : 채워야 하는 예산
    # 완전탐색
    
    d.sort()
    d_length = len(d)
    mx_cnt = 0
        
    # 나올 수 있는 모든 부분 집합의 경우의 수 : 2^n (공집합 포함)
    for i in range(1, 1<<d_length): # i : 1 ~ 2^d_length - 1
        for j in range(d_length): # j : 0 ~ d_length
            pass
        
    
#     while 1:
#         if i == (d_length - mx_cnt):
#             break

#         cnt = 0 # 지원할 수 있는 부서의 개수
        
#         for j in range(i, d_length):
#             pass
#         i += 1

    answer = 0
    return answer
