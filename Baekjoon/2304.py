n = int(input())    # 기둥의 개수
lst = []

for _ in range(n):
    a, b = map(int, input().split())
    lst.append((a, b))
# lst : [(2, 4), (11, 4), (15, 8), (4, 6), (5, 3), (8, 10), (13, 6)] (인덱스, 높이)

lst.sort(key=lambda x:x[0]) # 인덱스 순서로 정렬
# [(2, 4), (4, 6), (5, 3), (8, 10), (11, 4), (13, 6), (15, 8)]

mx = max(lst, key=lambda x:x[1])
mx_idx = lst.index(mx)  # 최대 높이인 기둥의 인덱스 값

# 기둥 기준 세 부분으로 나누기
left = lst[:mx_idx+1]
right = lst[mx_idx:][::-1]
# left : [(2, 4), (4, 6), (5, 3), (8, 10)]
# right : [(15, 8), (13, 6), (11, 4), (8, 10)]

res = 0
height = 0

# 왼쪽
for i in range(len(left)-1):
    height = max(left[i][1], height)
    if left[i][1] < left[i+1][1]:
        res += (left[i+1][0] - left[i][0]) * height
    else:
        res += (left[i+1][0] - left[i][0]) * height

# 오른쪽
height = 0
for i in range(len(right)-1):
    height = max(right[i][1], height)
    if right[i][1] < right[i + 1][1]:
        res += (right[i][0] - right[i+1][0]) * height
    else:
        res += (right[i][0] - right[i+1][0]) * height

# 최대높이 기둥 더함
res += lst[mx_idx][1]

print(res)

