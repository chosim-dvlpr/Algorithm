def solution(left, right):
    answer = 0
    # 약수 개수가 짝수 => 더하기
    # 약수 개수가 홀수 => 빼기
    num = left
    
    for n in range(left, right+1):
        i = 0
        cal = n # i가 순회할 마지막 값
        cnt = 0 # 약수의 개수
        
        if n == 1:
            cnt = 1
        else:
            while i < cal-1:
                i += 1
                if n % i == 0: # 나눠지면
                    if  i ** 2 != n: # 제곱수가 아니라면
                        cnt += 2
                    else: # 제곱수일때
                        cnt += 1 
                    cal = n // i # 최대값을 나눈 몫으로 바꿈

        if cnt % 2: # 약수가 홀수개면
            answer -= n
        else: # 약수가 짝수개면
            answer += n        

    return answer
