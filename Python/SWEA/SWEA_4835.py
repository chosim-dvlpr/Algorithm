T = int(input())

for test_case in range(T):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    new_list = []
    for idx in range(N - M + 1):
        sums = 0
        for num in range(M):
            sums += a[idx + num]
        new_list += sums

    maxs = new_list[0]
    mins = new_list[0]

    for n in range(len(new_list)):
        if new_list[n] >= maxs:
            maxs = new_list[n]
        if new_list[n] <= mins:
            mins = new_list[n]
    print(f'#{test_case + 1} {maxs - mins}')