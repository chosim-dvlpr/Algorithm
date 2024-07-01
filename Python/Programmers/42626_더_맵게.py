import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    
    while len(scoville) > 1:
        first = heapq.heappop(scoville)
        if first >= K: break
        
        second = heapq.heappop(scoville)
        newScoville = first + second * 2
        heapq.heappush(scoville, newScoville)
        answer += 1
        
    if len(scoville) == 1 and scoville[0] < K:
        return -1
    
    return answer
