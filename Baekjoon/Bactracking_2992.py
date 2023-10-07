# x와 구성이 같으면서 x보다 큰 수 중 가장 작은 수 구하기
# 수를 이루고 있는 각 자릿수가 같음
# 123, 321은 수의 구성이 같지만
# 123과 432는 구성이 같지 않음
# 그러한 숫자가 없다면 0 출력

x = input()
lst = list(x)
L = len(x)
visited = [0] * L
res = []

def bt(st, idx, visited):
    global res

    if idx == L:
        if int(x) < int(st):
            res.append(int(st))
        return
    
    for i in range(L):
        if not visited[i]:
            visited[i] = 1
            bt(st+lst[i], idx+1, visited)
            visited[i] = 0

bt('', 0, visited)
if res: # 값이 있을 때
    print(min(res))
else:
    print(0)
