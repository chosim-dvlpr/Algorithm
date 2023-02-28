import sys
n = int(sys.stdin.readline())

# 32비트 기준으로 보수 찾기

st = format(n, 'b') # 이진수

st = '0'*(32-len(st)) + st

res = ''
for word in st:
    if word == '0':
        res += '1'
    else:
        res += '0'
total = int(res, 2) + 1
bin_total = format(total, 'b')

cnt = 0
for x, y in zip(st, str(bin_total)):
    if x != y:
        cnt += 1
print(cnt)