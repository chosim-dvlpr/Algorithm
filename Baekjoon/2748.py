import sys

def fibo(k):
    global cnt      # 전역변수 받아줌 (cnt는 n번째 피보나치 수)
    f = [0]*(k+1)   # 0으로 채워진 배열 생성
    f[0] = 0        # 초기값 설정 (0, 1)
    f[1] = 1
    for i in range(2, k+1):     # 초기값 설정 후 2부터 k까지 순회하며 더함
        f[i] = f[i-1] + f[i-2]  # i번째 피보나치 수는 i-1, i-2번째 수의 합
        cnt += 1                # n+1번째 피보나치 수
        if cnt == n:            # cnt가 n과 같다면 멈춤
            break
    return f[k]     # n번째에서 멈췄으므로 이때의 f[k]값 반환

n = int(sys.stdin.readline()) # n은 2 이상의 자연수
cnt = 1                       # 2번째 피보나치부터 진행하므로 cnt는 1로 설정해줌
print(fibo(n))