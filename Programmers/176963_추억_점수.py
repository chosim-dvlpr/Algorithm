def solution(name, yearning, photo):
    answer = []
    
    for i in range(len(photo)):
        total = 0 # 합계
        for j in range(len(photo[i])):
            try:
                idx = name.index(photo[i][j])
                total += yearning[idx]
            except:
                pass
        answer.append(total)
            
    return answer
