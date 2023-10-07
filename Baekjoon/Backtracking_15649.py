# n까지의 자연수 중 중복 없이 m개를 고른 수열

n, m = map(int, input().split())
visited = [0] * (n+1)
res = []

# def bt(idx, visited):
#     global res
#     if idx == m:
#         print(res)
#         return
    
#     for i in range(n):
#         if not visited[i]:
#             visited[i] = 1
#             res.append(i+1)
#             bt(idx+1, visited)
#             visited[i] = 0

def bt(res, idx, visited):
    if idx == m:
        if len(res) == m:
            print(*res)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            
            bt(res.append(i+1), idx+1, visited)
            visited[i] = 0


bt(res, 0, visited)