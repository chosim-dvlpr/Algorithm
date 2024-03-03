# 최솟값 구하기 => - 뒤쪽은 묶어서 전부 뺴주면 됨

import sys
input = sys.stdin.readline

st = input().strip()
arr = st.split('-')
sums = 0

if st[0] == '-':
    sums -= int(arr[0])
else:
    sums += sum(list(map(int, arr[0].split('+'))))

for i in range(1, len(arr)):
    temp = list(map(int, arr[i].split('+')))
    sums -= sum(temp)
print(sums)
        