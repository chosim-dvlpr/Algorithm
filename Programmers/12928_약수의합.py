def solution(n):
    answer = 0
    end = n // 2
    a = 0
    b = 0
    
    while 1:
        a += 1    
        if n % a == 0: # 딱 떨어질 때
            b = n / a        
            answer += int(a + b)
        print(a, b, answer)
        if a == end:
            break
    
    return answer
