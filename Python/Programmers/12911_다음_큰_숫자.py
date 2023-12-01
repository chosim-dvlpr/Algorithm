# n의 다음 큰 숫자 정의
# n보다 큰 자연수
# 2진수로 변환했을 때 n와 다음큰숫자의 1의 개수가 같음
# 위 조건 만족하는 수 중 가장 작은 수

# 10진수 -> 2진수 변환 및 1 개수 확인
def checkBin(n, k):
    binN = bin(n)[2:]
    binK = bin(k)[2:]
    
    N_cnt = 0
    K_cnt = 0
    for i in range(len(binN)):
        if binN[i] == '1':
            N_cnt += 1
    for i in range(len(binK)):
        if binK[i] == '1':
            K_cnt += 1
        if K_cnt > N_cnt:
            return False
    if K_cnt != N_cnt:
        return False
    return True
   
def solution(n):
    k = n+1
    while not checkBin(n, k):
        k += 1
        
    return k
