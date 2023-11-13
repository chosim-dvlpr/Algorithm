def solution(citations):
    citations.sort(reverse = True)
    answer = 0
    for i in range(len(citations)): # 인용횟수가 많은 논문부터 순회
        if citations[i] > answer: # 만약 i번째로 인용횟수가 많은 논문의 횟수가 현재 h-index(answer)보다 많다면
            answer = i+1 # 순회를 돈 논문 개수
        else:
            break
    return answer
