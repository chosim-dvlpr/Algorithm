def solution(name, yearning, photo):
    answer = []

    # [1] try - except 구문
    
    # for i in range(len(photo)):
    #     total = 0 # 합계
    #     for j in range(len(photo[i])):
    #         try:
    #             idx = name.index(photo[i][j])
    #             total += yearning[idx]
    #         except:
    #             pass
    #     answer.append(total)
    
    
    # [2] dictionary 이용
    
    # name과 score를 풀어(zip) dict 형태로 만듦
    name_score = dict(zip(name, yearning))
    
    for i in range(len(photo)):
        total = 0 # 합계
        for j in range(len(photo[i])):
            # photo[i][j]라는 key가 있다면 0 이상의 값 반환
            # key가 없다면 -1 반환
            res = name_score.get(photo[i][j], -1)
            if res > -1:
                total += res
        answer.append(total)
        
    return answer
