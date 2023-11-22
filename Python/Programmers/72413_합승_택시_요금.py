# a 지점과 b 지점을 모두 방문했을 때 나오는 값의 최솟값 구하기
# 해당 최솟값과 a와 b 지점을 각각 방문했을때의 합과 비교
# 더 작은 값이 최종 답
# n : 노드 개수
# s : 출발지점
import heapq

def solution(n, s, a, b, fares):
    INF = 9876543210
    answer = INF
    graph = [[] for _ in range(n+1)]
    
    # start -> end 요금을 담은 graph
    # graph[출발점] = (종료지점, 비용)
    # 양방향
    for fare in fares:
        start, end, fee = fare
        graph[start].append((end, fee))
        graph[end].append((start, fee))
    
    def dijkstra(s):
        q = []
        distance = [INF] * (n+1) # 최단거리 배열
        heapq.heappush(q, (0, s)) # q에 (비용, 노드번호) 저장
        distance[s] = 0 # 시작노드의 비용을 0으로 저장
        
        while q:
            dist, curr = heapq.heappop(q)
            # 현재 노드가 이미 처리된 노드면 무시
            if distance[curr] < dist: 
                continue
            
            for g in graph[curr]:
                # g : (curr에서 갈 수 있는 노드 번호, 해당 노드까지의 비용)
                cost = dist + g[1]
                # 최단거리 갱신
                if cost < distance[g[0]]:
                    distance[g[0]] = cost
                    # q에 (현재 비용, 도착지점 노드번호) 저장
                    heapq.heappush(q, (cost, g[0]))
        return distance
    
    distance_list = [[]] + [dijkstra(i) for i in range(1, n+1)]
    for i in range(1, n+1):
        answer = min(distance_list[s][i] + distance_list[i][a] + distance_list[i][b], answer)
    
    return answer
