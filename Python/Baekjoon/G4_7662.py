import sys
from heapq import heappush, heappop
input = sys.stdin.readline

tc = int(input())


for _ in range(tc):
    N = int(input())

    isDeleted = [False] * N
    maxHeap = []
    minHeap = []
    
    for n in range(N):
        calc, num = input().strip().split(' ')
        if calc == 'I':
            heappush(maxHeap, (-int(num), n))
            heappush(minHeap, (int(num), n))
        elif num == '1' and maxHeap: # 최댓값 삭제
            while maxHeap and isDeleted[maxHeap[0][1]]:
                heappop(maxHeap)
            if maxHeap:
                value, key = heappop(maxHeap)
                isDeleted[key] = True
        elif num == '-1' and minHeap: # 최솟값 삭제
            while minHeap and isDeleted[minHeap[0][1]]:
                heappop(minHeap)
            if minHeap:
                value, key = heappop(minHeap)
                isDeleted[key] = True

    while maxHeap and isDeleted[maxHeap[0][1]]:
        heappop(maxHeap)
    while minHeap and isDeleted[minHeap[0][1]]:
        heappop(minHeap)


    if not maxHeap:
        print('EMPTY')
    else:
        print(-maxHeap[0][0], minHeap[0][0])

