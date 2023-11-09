mx = 0

# 순열 (순서 상관 O)
def permentation(n, visited, st, numbers):
    global mx

    if st != '' and sum(visited) == n and int(st) >= mx:
        mx = int(st)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            permentation(n, visited, st+str(numbers[i]), numbers)
            visited[i] = 0
    
    

def solution(numbers):
    # 원소가 0일 때 => 제외
    n = len(numbers)
    visited = [0] * n
    
    permentation(n, visited, '', numbers)
    
    return str(mx)
