# a의 가장 큰 값과 b의 가장 작은 값을 서로 곱하기
def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    
    l = len(A)
    idx = 0
    while 1:
        if idx == l:
            return answer
        answer += A[idx] * B[idx]
        idx += 1
    return
