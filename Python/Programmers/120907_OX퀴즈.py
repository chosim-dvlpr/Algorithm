def solution(quiz):
    answer = []
    
    for q in quiz:
        eq = q.find("=") # 등호 위치
        
        for i in range(len(q)):
            if i != 0 and q[i] == "-" or q[i] == "+":
                pm = i # 플러스 or 마이너스 인덱스
                break
                
        x = int(q[:pm-1])
        y = int(q[pm+2:eq-1])
        z = int(q[eq+2:])
        
        if q[pm] == "-":
            data = (x - y == z)
        else:
            data = (x + y == z)

        if data: # true일 때
            answer.append("O")
        else:
            answer.append("X")
        
    return answer
