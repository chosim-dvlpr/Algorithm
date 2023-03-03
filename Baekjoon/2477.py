# 참외밭
# 1m2에서 자라는 참외의 개수 => 참외의 총개수 구함
# 참외밭의 넓이
# 임의의 한 꼭짓점에서 출발, 반시계로 둘레를 돌게됨
# 참외밭에서 자라는 참외의 수를 구하시오

n = int(input())    # 1m2에 자라는 참외의 개수
lst = []
for _ in range(6):  # 변의 방향과 길이, 반시계 방향
    a, b = map(int, input().split())
    lst.append((a, b))  # 동1 서2 남3 북4
# lst : [(2, 5), (3, 5), (1, 1), (4, 2), (1, 4), (4, 3)]

# si : 세로, sj : 가로
dot = [(0, 0)]
si = sj = 0     # 첫 번째 점

for i in range(len(lst)-1):
    if lst[i][0] == 1:
        sj += lst[i][1]
        dot.append((si, sj))
    elif lst[i][0] == 2:
        sj -= lst[i][1]
        dot.append((si, sj))
    elif lst[i][0] == 3:
        si -= lst[i][1]
        dot.append((si, sj))
    else:
        si += lst[i][1]
        dot.append((si, sj))

# dot : [(0, 0), (0, -160), (30, -160), (30, -100), (50, -100), (50, 0)]

dot_jmax = sorted(dot, key=lambda x:x[1])
dot_imax = sorted(dot, key=lambda x:x[0])

left_top = (dot_imax[-1][0], dot_jmax[0][1])
right_top = (dot_imax[-1][0], dot_jmax[-1][1])
left_bottom = (dot_imax[0][0], dot_jmax[0][1])
right_bottom = (dot_imax[0][0], dot_jmax[-1][1])


temp = []
for i in dot:
    if i not in (left_top, left_bottom, right_top, right_bottom):
        temp.append(i)

temp.sort(key=lambda x:(x[0], x[1]))    # i좌표 순 -> j좌표 순으로 정렬
# temp : [(20, -160), (20, -100), (50, -160)]

total_rec = abs((left_top[1] - right_top[1]) * (left_top[0] - left_bottom[0]))
if temp[0][1] != temp[1][1]:
    a = temp[0][1] - temp[1][1]
else:
    a = temp[0][1] - temp[-1][1]
small_rec = abs((temp[0][0]-temp[-1][0]) * a)
res = total_rec - small_rec

print(res*n)