def solution(participant, completion):
    dic = {}
    for c in completion:
        dic[c] = 0
    
    for p in participant:
        temp = dic.get(p, -1)
        if temp == -1:
            return p
        dic[p] += 1
        
    return 
