# f(0) = 0
# f(1) = 1
# f(2) = 1
# f(3) = 2
# 피보나치
# n번째 피보나치수를 구하기

n = int(input())
f = [0] * (10001)

f[1] = 1
f[2] = 1

for i in range(3, n+1):
    f[i] = f[i-2] + f[i-1]
print(f[n])