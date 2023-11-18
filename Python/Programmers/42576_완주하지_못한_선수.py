def solution(participant, completion):
    dic = {}
    for p in participant:
        temp = dic.get(p, -1)
        # 아직 key로 안들어가있을 때, 중복이 아닌 상태
        if temp == -1:
            dic[p] = 1
        # key로 이미 들어가있을 때, 중복문자
        else:
            dic[p] += 1
    
    for c in completion:
        dic[c] -= 1
    
    for d in dic.keys():
        if dic[d] > 0:            
            return d
        
    return 
