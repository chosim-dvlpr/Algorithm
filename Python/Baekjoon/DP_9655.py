# 돌 n개
# 돌 1개 또는 3개 가져감
# 마지막 돌을 가져가면 이김
# 이기는 사람 구하기
# 상근이 먼저 시작
# 상근 : SK, 창영 : CY

n = int(input())

# 풀이 1
# if n%2: # 홀수
#     print("SK")
# else:
#     print("CY")

# 풀이 2
win = [-1] * (1001)

# SK : 1
# CY : 0
# 시작 시 
# 상근이 1개 가져감 => 창영은 n = 2부터 시작
# 상근이 3개 가져감 => 창영은 n = 4부터 시작

win[1] = 1
win[2] = 0
win[3] = 1

for i in range(4, n+1):
    if win[i-1] or win[i-3]:
        win[i] = 0
    else:
        win[i] = 1

print("CY" if win[n] == 0 else "SK")