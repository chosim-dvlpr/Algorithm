# n : 도감에 수록된 포켓몬의 개수
# m : 맞춰야 하는 문제의 개수
# 포켓몬의 이름 : 영어, 첫 글자만 대문자 (2~20)
# 일부 포켓몬은 마지막 문자만 대문자
# 알파벳으로 들어오면 포켓몬 번호 출력
# 숫자로 들어오면 문자 출력

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
lst = deque([])

for _ in range(n):
  lst.append(input().strip())

for _ in range(m):
  quiz = input().strip()
  if quiz.isnumeric():
    print(lst[int(quiz)-1])
  else:
    print(lst.index(quiz)+1)

  


# lst = dict()

# for i in range(1, n+1):
#   lst[str(i)] = input().strip()

# for _ in range(m):
#   quiz = input().strip()
#   for key, value in lst.items():
#     if quiz == key:
#       print(value)
#     elif quiz == value:
#       print(key)
#   # quiz = input().strip()

#   # if quiz.isnumeric():
#   #   print(lst[int(quiz)])
#   # else:
#   #   print(lst[index(quiz)])
