def solution(n):
    # n이 1 또는 2일 때, 각각 1와 2 한 가지 케이스만 존재
    # 런타임 에러 방지 위해 초기에 return,
    # n이 2보다 클 때 배열을 만듦
    if n <= 2:
        return n
    elif n > 2:
        arr = [0] * (n+1)
        arr[1] = 1
        arr[2] = 2
        for i in range(3, n+1):
            arr[i] = arr[i-1] + arr[i-2]
    return arr[n] % 1234567
