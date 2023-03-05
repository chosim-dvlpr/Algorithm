'''
m, n : 종이의 가로 세로 길이
cut : 종이를 자르는 횟수
0 : 가로로 자름
1 : 세로로 자름
가장 큰 종이 조각의 넓이를 출력하기

점선 번호 = 칸의 개수
'''

m, n = map(int, input().split())
cut = int(input())
row = []
col = []

for _ in range(cut):
    a, b = map(int, input().split())
    if a == 0:  # 가로로 자르는 선일 때
        row.append(b)
    else:       # 세로로 자르는 선일 때
        col.append(b)

row.append(0)
row.append(n)
col.append(0)
col.append(m)

row.sort()
col.sort()

sub_row = []
sub_col = []

for i in range(1, len(row)):
    sub_row.append(row[i] - row[i-1])
for i in range(1, len(col)):
    sub_col.append(col[i] - col[i-1])

area = []
for i in range(len(sub_row)):
    for j in range(len(sub_col)):
        a = sub_row[i] * sub_col[j]
        area.append(a)
print(max(area))