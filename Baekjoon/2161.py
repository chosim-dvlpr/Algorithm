from collections import deque

def solution (end):
  answer = []
  # q = deque()
  q = deque(_ for _ in range(1, end+1))

  flag = 1 # 버리기

  while 1:
    if flag: # 버리는 동작
      answer.append(q.popleft())
      flag = 0
    else: # 밑으로 내리는 동작
      q.append(q.popleft())
      flag = 1

    # q 길이가 한 개만 남게 되면 answer에 추가
    if len(q) == 1:
      answer.append(q[0])
      break
  return answer


end = int(input())

for n in solution(end):
  print(n, end=" ")
