def solution(d, budget):
    # d : 예산 리스트
    # budget : 가능한 최대 예산 (부족해도 됨)
    # 완전탐색
    
    d.sort()
    answer = 0

    for i, part in enumerate(d):
        budget -= part

        if budget < 0:
            answer = i
            break
        elif budget == 0:
            answer = i+1
            break

                    
    return answer
