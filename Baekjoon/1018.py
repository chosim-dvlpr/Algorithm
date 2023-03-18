'''
m*n 크기의 보드 (m : 가로, n : 세로)
보드를 잘라 8*8 크기로 만들고자 함
**규칙**
검은색과 흰색이 번갈아 칠해져 있어야
왼쪽위칸이 흰색인 경우/검은색인 경우

8*8 크기로 자른 뒤 다시 칠해야 하는 정사각형의 최소 개수는?
'''


'''
def func(lst, start):
    cnt = 0
    if start == 'W':
        for x in range(len(lst)):
            if x % 2:  # x가 홀수일 때 : 홀수번째 인덱스 확인
                for y in range(len(lst[x])):
                    if y % 2:  # y가 홀수일 때
                        if lst[x][y] == 'B':
                            cnt += 1
                    else:  # y가 짝수일 때
                        if lst[x][y] == 'W':
                            cnt += 1
            else:  # x가 짝수일 때 : 짝수번째 인덱스 확인
                for y in range(len(lst[x])):
                    if y % 2:
                        if lst[x][y] == 'W':
                            cnt += 1
                    else:
                        if lst[x][y] == 'B':
                            cnt += 1
    else:   # 첫문자가 B일때
        for x in range(len(lst)):
            if x % 2:  # x가 홀수일 때 : 홀수번째 인덱스 확인
                for y in range(len(lst[x])):
                    if y % 2:  # y가 홀수일 때
                        if lst[x][y] == 'W':
                            cnt += 1
                    else:  # y가 짝수일 때
                        if lst[x][y] == 'B':
                            cnt += 1
            else:  # x가 짝수일 때 : 짝수번째 인덱스 확인
                for y in range(len(lst[x])):
                    if y % 2:
                        if lst[x][y] == 'B':
                            cnt += 1
                    else:
                        if lst[x][y] == 'W':
                            cnt += 1
    return cnt
'''


def func(lst):
    global res
    color = ['W', 'B']
    for c in color:
        cnt = 0
        for x in range(len(lst)):
            if x%2: # 홀수일 때
                for y in range(len(lst)):
                    if y % 2:   # 홀수일 때
                        if lst[x][y] == c:
                            cnt += 1
                    else:
                        if lst[x][y] != c:
                            cnt += 1
            else:   # 짝수일 때
                for y in range(len(lst)):
                    if y % 2:
                        if lst[x][y] != c:
                            cnt += 1
                    else:
                        if lst[x][y] == c:
                            cnt += 1
        res.append(cnt)


n, m = map(int, input().split())
board = []
res = []    # 칠해야 하는 개수

for _ in range(n):
    a = input()
    board.append(a)
# board : ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBBBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']


for k in range(n-8+1):
    for j in range(m-8+1):
        lst = []
        cnt = 0
        for i in range(8):
            # for k in range(8):
            b = board[i+k][j:j+8]
            lst.append(b)
        # lst : ['BBBBBBBB', 'BBBBBBBB', 'BBBBBBBB', 'BBBBBBBB', 'BBBBBBBB', 'BBBBBBBB', 'BBBBBBBB', 'BBBBBBBB']

        func(lst)
print(res)
print(min(res))








'''
for i in range(n-8+1):
    for j in range(m-8+1):
        cnt = 0
        for k in range(8):
            b = board[i+k][j:j+8]   # 가로 -> 세로
            # 첫 번째 칸이 W일때
            if board[i+k][j] == 'W':
                for x in range(0, 8, 2):    # 짝수번째 인덱스
                    if board[i+k][j:j+8][x] != 'W':
                        cnt += 1
            else:
                for x in range(1, 8, 2):    # 홀수번째 인덱스
                    if board[i+k][j:j+8][x] != 'B':
                        cnt += 1
        lst.append(cnt)
'''
