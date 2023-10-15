def solution(n):
    answer = 0
    
    arr = [0] * 3001
    if n > 1:
        for i in range(1, n+1):
            if arr[i] == 1:
                break
            elif arr[i] == 0 and n % i == 0: # 딱 떨어질 때
                if i != n//i: # 제곱수가 아닐때
                    answer += i + n//i
                else:
                    answer += i
                    break
                arr[n//i] = 1 # 몫을 1로 바꿈
    elif n == 1:
        answer = 1
    
    return answer
