def sums(num_list):
    cnt = 0
    for num in num_list:
        cnt += num
    return cnt


for _ in range(10):
    tc = int(input())
    arr = []
    for i in range(100):
        arr.append(list(map(int, input().split()))) # 1행씩 리스트에 리스트로 넣음

    maxs = -1

    # 행 탐색, 행 별 합계의 최대값 저장
    for i in range(len(arr)):
        if sums(arr[i]) > maxs:
            maxs = sums(arr[i])

    # 열 탐색, 최대값 저장
    for i in range(len(arr[0])):
        sums_list = []  # 각 행/열/대각선의 합계를 넣을 리스트
        diagonal_list = []
        rev_diagonal_list = []
        for j in range(len(arr[0])):
            sums_list.append(arr[j][i])
            if i == j:
                diagonal_list.append(arr[i][i])
                rev_diagonal_list.append(arr[(len(arr)-1)-i][i])
                
        if sums(sums_list) > maxs:
            maxs = sums(sums_list)
        if sums(diagonal_list) > maxs:
            maxs = sums(diagonal_list)
        if sums(rev_diagonal_list) > maxs:
            maxs = sums(rev_diagonal_list)

    print(f'#{tc} {maxs}')
