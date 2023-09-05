def solution(quiz):
    answer = []
    
    for q in quiz:
        eq = q.index("=") # 등호 위치
        left = q[:eq-1] # 공백 제거
        right = int(q[eq+2:]) # 공백 제거

        for i in range(len(left)):
            if left[i] == "-" or left[i] == "+":
                pm = i # 플러스 or 마이너스 인덱스
        x = int(left[:pm-1])
        y = int(left[pm+2:])
        
        def cal(data):
            if data == "-":
                if (x - y == right):
                    return "O"
            else:
                if (x + y == right):
                    return "O"
            return "X"    
        
        answer.append(cal(left[pm]))
        
    return answer
