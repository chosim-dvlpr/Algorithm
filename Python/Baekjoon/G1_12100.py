# 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값

import sys, copy
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

if n == 1:
    print(arr[0][0])
else:
    # 가로 이동
    def horizontal(move, arr):
        graph = copy.deepcopy(arr)
        if move == 'left':
            for i in range(len(graph)):
                temp = []
                for j in range(len(graph[i])):
                    if graph[i][j] != 0:
                        temp.append(graph[i][j])
                graph[i] = temp + [0] * (n - len(temp))
                for j in range(n-1):
                    if graph[i][j] == graph[i][j+1] and graph[i][j] != 0:
                        graph[i][j] *= 2
                        graph[i][j+1] = 0
                temp = []
                for j in range(len(graph[i])):
                    if graph[i][j] != 0:
                        temp.append(graph[i][j])
                graph[i] = temp + [0] * (n - len(temp))
        else:
            for i in range(len(graph)):
                temp = []
                for j in range(len(graph[i])):
                    if graph[i][j] != 0:
                        temp.append(graph[i][j])
                graph[i] = [0] * (n - len(temp)) + temp
                for j in range(n-1, 0, -1):
                    if graph[i][j] == graph[i][j-1]:
                        graph[i][j] *= 2
                        graph[i][j-1] = 0
                temp = []
                for j in range(len(graph[i])):
                    if graph[i][j] != 0:
                        temp.append(graph[i][j])
                graph[i] = [0] * (n - len(temp)) + temp

        return graph

    # 세로 이동
    def vertical(move, arr):
        graph = copy.deepcopy(arr)
        if move == 'up':
            for j in range(n):
                start = 1
                idx = 0
                while start < n and idx < n:
                    if graph[idx][j] != 0:
                        idx += 1
                        start = idx+1
                    elif graph[idx][j] == 0 and graph[start][j] != 0:
                        graph[idx][j] = graph[start][j]
                        graph[start][j] = 0
                        idx += 1
                        start = idx + 1
                    elif graph[idx][j] == 0 and graph[start][j] == 0:
                        start += 1
            for i in range(n-1):
                for j in range(n):
                    if graph[i][j] == graph[i+1][j]:
                        graph[i][j] *= 2
                        graph[i+1][j] = 0
            for j in range(n):
                start = 1
                idx = 0
                while start < n and idx < n:
                    if graph[idx][j] != 0:
                        idx += 1
                        start = idx+1
                    elif graph[idx][j] == 0 and graph[start][j] != 0:
                        graph[idx][j] = graph[start][j]
                        graph[start][j] = 0
                        idx += 1
                        start = idx + 1
                    elif graph[idx][j] == 0 and graph[start][j] == 0:
                        start += 1
            
                    
        else:
            for j in range(n):
                start = n-2
                idx = n-1
                while start >= 0 and idx >= 0:
                    if graph[idx][j] != 0:
                        idx -= 1
                        start = idx-1
                    elif graph[idx][j] == 0 and graph[start][j] != 0:
                        graph[idx][j] = graph[start][j]
                        graph[start][j] = 0
                        idx -= 1
                        start = idx - 1
                    elif graph[idx][j] == 0 and graph[start][j] == 0:
                        start -= 1
            for i in range(n-1, 0, -1):
                for j in range(n):
                    if graph[i][j] == graph[i-1][j]:
                        graph[i][j] *= 2
                        graph[i-1][j] = 0
            for j in range(n):
                start = n-2
                idx = n-1
                while start >= 0 and idx >= 0:
                    if graph[idx][j] != 0:
                        idx -= 1
                        start = idx-1
                    elif graph[idx][j] == 0 and graph[start][j] != 0:
                        graph[idx][j] = graph[start][j]
                        graph[start][j] = 0
                        idx -= 1
                        start = idx - 1
                    elif graph[idx][j] == 0 and graph[start][j] == 0:
                        start -= 1
            
        return graph
            
    def checkMax(a):
        mx = 0
        for i in a:
            mx = max(mx, max(i))
        return mx

    def moveBlock(cnt, a, b):
        global res

        if cnt == 5:
            temp = checkMax(a)
            if res < temp:
                res = temp
            return
        
        for m in mode:
            if m == 'up' or m == 'down':
                moveBlock(cnt+1, vertical(m, a), b+[m])
            else:
                moveBlock(cnt+1, horizontal(m, a), b+[m])

    res = 0
    mode = ['up', 'down', 'left', 'right']
    moveBlock(0, arr, [])

    print(res)