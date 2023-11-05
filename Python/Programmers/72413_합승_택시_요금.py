# a 지점과 b 지점을 모두 방문했을 때 나오는 값의 최솟값 구하기
# 해당 최솟값과 a와 b 지점을 각각 방문했을때의 합과 비교
# 더 작은 값이 최종 답
# n : 노드 개수
# s : 출발지점
import heapq
mx = 9876543210

def dijkstra(n, arr, s):
    distance = [mx for _ in range(n+1)]
    distance[s] = 0 # 자기 자신은 제외
    q = [[s, 0]] # [출발 인덱스, 누적 요금]
    
    while q:
        print(q)
        curr, dist = heapq.heappop(q)
        # if distance[curr] < dist:
            # continue
        for i in arr[curr]:
            cost = distance[curr] + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))
    return distance
        
        
#         departure, fee = heappop(start)
#         print("for문 이전 : ", departure, fee)
#         for arrive, fee2 in arr[departure]:
#             print(arrive, fee2)
#             fee2 += fee # 누적합
#             # 최솟값 찾기
#             if lst[arrive] > fee2:
#                 lst[arrive] = fee2
#                 heappush(start, [arrive, fee2])
#     print(lst)
#     return lst
            
        
def solution(n, s, a, b, fares):
    # i = 노드번호, arr[i] = [(연결된 노드번호, 금액)]
    arr = [[] for _ in range(n+1)]
    for fare in fares:
        arr[fare[0]].append((fare[1], fare[2]))
        arr[fare[1]].append((fare[0], fare[2]))
    
    # s부터 시작하는 최소 이동 거리 구하기
    distance = dijkstra(n, arr, s)
