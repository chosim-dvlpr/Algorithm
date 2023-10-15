import sys
T = int(sys.stdin.readline())

# 내장함수 사용한 풀이
for tc in range(1, T+1):
    N = int(sys.stdin.readline())
    beer_lst = []
    for i in range(N):
        S, L = sys.stdin.readline().split()
        beer_lst.append([S, int(L)])
    beer_lst.sort(key=lambda x:x[1], reverse=True)
    print(beer_lst[0][0])


'''
# 내장함수 사용하지 않고 풀이
for tc in range(1, T+1):
    N = int(sys.stdin.readline())
    univ = []
    beer = []
    for i in range(N):
        S, L = sys.stdin.readline().split()
        univ.append(S)
        beer.append(int(L))
    maxs = beer[0]
    max_idx = 0
    for i in range(N):
        if maxs < beer[i]:
            maxs = beer[i]
            max_idx = i
    print(univ[max_idx])
'''