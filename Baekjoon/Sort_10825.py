# n : 학생 수 
# name, lan, eng, math : 이름, 국어, 영어, 수학 점수

'''
정렬 순서

국어 점수가 감소하는 순서로
국어 점수가 같으면 영어 점수가 증가하는 순서로
국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)
'''

import sys
input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
  lst.append(input().split())
  
  # name, lan, eng, math = map(str, input().split())
  # lst.append([name, int(lan), int(eng), int(math)])

lst.sort(key=lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
# lst.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))

for i in lst:
  print(i[0])