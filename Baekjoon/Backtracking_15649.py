# n까지의 자연수 중 중복 없이 m개를 고른 수열

n, m = map(int, input().split())
lst = [_ for _ in range(1, n+1)]
visited = [0] * (n+1)
res = []

def bt(idx, visited):
    global res

    # idx가 뽑아야 하는 개수와 같아질 때
    if idx == m:
        if len(res) == m: # 출력할 리스트 개수가 m과 같을 때 출력
            print(*res)
        return
    
    for i in range(1, n+1):
        if not visited[i]: # 방문하지 않았다면 방문표시
            visited[i] = 1
            res.append(i)  # res에 추가해두고
            bt(idx+1, visited) # 재귀
            res.pop()      # res 원상복구
            visited[i] = 0 # 방문표시 원상복구


bt(0, visited)