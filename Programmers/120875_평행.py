def solution(dots):
    answer = 0
    
    for i in range(1, len(dots)):
        grad1 = (dots[0][1] - dots[i][1])/(dots[0][0] - dots[i][0])
        if i == 1:
            a, b = 2, 3
        elif i == 2:
            a, b = 1, 3
        else:
            a, b = 1, 2
        grad2 = (dots[a][1] - dots[b][1])/(dots[a][0] - dots[b][0])
        
        if grad1 == grad2: # 평행이라면
            answer = 1
            return answer
        
    return answer
