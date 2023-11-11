def solution(citations):
    answer = 0
    citations.sort()
    
    for i, c in enumerate(citations):
        if len(citations[i:]) == c:
            answer = citations[i]
            break
        elif len(citations[i:]) < c:
            answer = citations[i-1]
            break
    
    return answer
