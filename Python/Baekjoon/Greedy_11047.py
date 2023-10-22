# n종류의 동전의 가치의 합을 k로 만들기
# 이때 필요한 동전 개수의 최솟값 구하기

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = []

for _ in range(n):
  lst.append(int(input()))

cnt = 0

def get_cnt(idx, k, cnt):
  if k == 0:
    print(cnt)
    return

  if idx < 0:
    return

  for i in range(idx, -1, -1):
    if lst[i] <= k:
      break
  
  get_cnt(i-1, k%lst[i], cnt+k//lst[i])

get_cnt(n-1, k, 0)

# for i in range(n-1, -1, -1):
#   if lst[i] < k:
#     break

# cnt += k // lst[i] # 4
# k = k % lst[i] # 200

# for i in range(i-1, -1, -1):
#   if lst[i] < k:
#     break

# cnt += k // lst[i] # 6
# k = k % lst[i] # 0

# if k == 0:
#   print(cnt)



# def get_sums(arr):
#   sums = 0
#   cnt = 0
#   for a in range(n):
#     if arr[a] == 1:
#       sums += lst[a]
#       cnt += 1
#       if sums > k:
#         return 0
#   print(sums)
#   if sums == k:
#     print("hihihi")
#     return cnt
#   else:
#     return 0


# def func(i, n):
#   global mn

#   if i == n:
#     cnt = get_sums(arr)
#     if cnt > 0:
#       if mn > cnt:
#         mn = cnt
#         return
#   else:
#     arr[i] = 0
#     func(i+1, n)
#     arr[i] = 1
#     func(i+1, n)

# func(0, n)
# print(mn)


# def func(idx, arr, cnt, sums):
#   global mn

#   if sums > k:
#     return
  
#   elif sums == k:
#     if mn > cnt:
#       mn = cnt
#     return
  
#   else:
#     arr[idx] = 1
#     for i in range(n):
#       if arr[i] == 1:
#         sums += lst[i]
#     func(idx+1, arr, cnt+1, sums)
#     arr[idx] = 0
#     func(idx+1, arr, cnt+1, sums)

# func(1, )
