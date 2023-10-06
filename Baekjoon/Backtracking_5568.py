# 카드 : 1~ 99
# n : 4 ~ 10
# n장 중 k장 선택 (2~4)
# 가로로 정수를 만듦
# 정수의 개수는?

import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
cards = [input().strip() for _ in range(n)]

card_list = []

def pick(st, n, picked):
  if n == k:
    pass



lst = [] # 문자열
for _ in range(n):
  lst.append(input().replace('\n', ''))

cnt = 0 # 만들 수 있는 정수의 개수
result = [] # 만든 정수 리스트
visited = [0]*n
st = ''

def bt(visited, i, k):
  select = [1, 0] # 뽑거나, 안뽑거나

  # 뽑은 횟수가 k와 같아지면
  if i == k:
    for idx in range(k):
      if visited[idx]: # 방문한 자리일 때
        print(lst[idx])
    print()
  else:
    for i in range(2):
      visited[i] = select[i] # 뽑거나, 안뽑거나
      bt(visited, i+1, k)
bt(visited, 0, k)

#   if i == n or i == k:
#     result.append(st)
#     return result
  
#   if not visited[i]:
#     st += lst[i]
#     visited[i] = 1 # 방문 표시
#     bt(i+1)
#     visited[i] = 0

# print(bt(0))
# print(result)