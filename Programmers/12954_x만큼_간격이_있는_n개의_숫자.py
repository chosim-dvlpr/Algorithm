def solution(x, n):
    # 등차수열
    answer = []
    ad = x  # 시작값
    while 1:
        answer.append(ad)
        ad += x # 초기값 더하기
        if len(answer) == n:
            break
    
    return answer
