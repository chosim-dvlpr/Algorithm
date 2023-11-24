# n을 k진수로 바꿨을 때 조건에 맞는 소수 개수가 몇 개인가?
# 소수에는 0이 포함되지 않음
# 소수를 10진법으로 보았을 때 소수여야 소수로 인정

# n을 k진수로 변환
# 0이 나오는 지점 찾기
# 해당 숫자를 10진법으로 바꿨을 때 소수인지 확인


def solution(n, k):
    # n -> k진수 변환
    def changeN(n, k):
        st = ''
        
        while n > 0:
            n, mod = divmod(n, k) # 몫, 나머지
            st += str(mod)
        return st[::-1]
    
    changed_N = changeN(n, k)
    
    # 소수인지 확인
    def checkNum(n):
        # 2부터 n의 제곱근까지 확인
        for i in range(2, int(math.sqrt(n))+1):
            if x % i == 0:
                return False
        return True
    
    # 0이 나오는 지점 찾기
    start = 0
    for i, s in enumerate(changed_N):
        if s == '0':
            new_st = changed_N[start:i]
            print(new_st)
            
    return 
