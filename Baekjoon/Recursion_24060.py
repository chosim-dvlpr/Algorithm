import sys

# a : 배열의 크기
# k : 저장 횟수
# 배열 a에서 k번째 저장되는 수를 출력하기
# 저장횟수가 k보다 작으면 -1 출력
A, K = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
answer = []

# 병합정렬 - 분할 과정
def merge_sort(lst):
  if len(lst) == 1:
    return lst
  
  mid = len(lst) // 2 # 중앙값
  
  left = lst[:mid]    # 중앙값의 앞쪽까지
  right = lst[mid:]   # 중앙값부터 끝까지
  
  # 배열 길이가 1이 될 때까지 왼쪽, 오른쪽 나눔
  left = merge_sort(left)
  right = merge_sort(right)

  i = j = 0

  res = [] # 병합한 결과를 저장할 리스트

  while len(left) > i or len(right) > j:
    if len(left) > i and len(right) > j:
      if left[i] <= right[j]: # 오른쪽이 더 클 때
        last = left[i]
        res.append(last)
        answer.append(last)
        i += 1
      else:  # 왼쪽이 더 클 때
        last = right[j]
        res.append(last)
        answer.append(last)
        j += 1
    elif len(left) > i: # 오른쪽을 다 소진한 경우 왼쪽만 저장
      last = left[i]      
      res.append(last)
      answer.append(last)
      i +=1
    elif len(right) > j: # 왼쪽을 다 소진한 경우 오른쪽만 저장
      last = right[j]
      res.append(last)
      answer.append(last)
      j += 1

  return res

merge_sort(a)

# answer에는 저장한 데이터가 순차적으로 쌓이므로 
# K-1 인덱스가 K번째로 저장된 값
if len(answer) >= K:
  print(answer[K-1])
else:
  print(-1)