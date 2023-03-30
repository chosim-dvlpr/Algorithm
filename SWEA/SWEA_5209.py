'''
각 제품의 공장별 생산비용 주어짐
전체 제품의 최소 생산 비용은?
- 한 공장 당 한 개의 제품 생산

n : 제품의 수
lst : 제품별, 공장별 생산비용
visited : 방문 표시
'''

def mn_charge(idx, charge):
    global mn
    if idx == n:
        mn = min(mn, charge)
    else:
        if charge > mn: # 비용이 최소값보다 크면
            return      # 불필요한 계산 줄임

        for i in range(n):
            if visited[i]:  # i를 이미 방문했을 때
                continue    # 다음 i로 넘어감
            else:
                visited[i] = True   # 방문 표시
                mn_charge(idx+1, charge+lst[idx][i])    # 인덱스+1값과 생산비용을 더한 값을 넘겨줌
                visited[i] = False  # 방문 표시를 다시 원래대로 돌려줌

for tc in range(1, int(input())+1):
    n = int(input())    # 제품의 수
    lst = [list(map(int, input().split())) for _ in range(n)] # 제품별, 공장별 생산비용
    # lst : [[73, 21, 21], [11, 59, 40], [24, 31, 83]]
    visited = [False] * n
    mn = 987654321
    mn_charge(0, 0)

    print(f'#{tc} {mn}')