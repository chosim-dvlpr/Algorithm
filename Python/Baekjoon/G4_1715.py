import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = [int(input()) for _ in range(n)]
heapq.heapify(heap)
sums = 0

if n == 1:
    print(0)
else:
    while len(heap) > 1:
        temp1 = heapq.heappop(heap)
        temp2 = heapq.heappop(heap)
        sums += temp1 + temp2
        heapq.heappush(heap, temp1+temp2)
    print(sums)





# print(heapq.nsmallest(1, heap))

# for i in range(n):


# arr = [int(input().strip()) for _ in range(n)]
# arr = heapq(arr)
# arr.sort()
# print(arr)

# if n == 1:
#     print(0)
# else:
#     res = arr[0] * (n-1)
#     print('시작 : ', res)
#     for i in range(1, n):
#         res += arr[i] * (n-i)
#         print(i, res)
#     print(res)