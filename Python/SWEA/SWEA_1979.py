T = int(input())
for test_case in range(T):
    n, k = map(int, input().split())

    board = [input().split() for _ in range(n)]
    cnt = 0

    # 가로방향 확인
    res_row = [] # 한 행씩 원소로 넣음
    for lst in board:
        res_row.append(''.join(map(str, lst)))
    res_row_spt = list(map(lambda x: x.split('0'), res_row))
    
    for nums in res_row_spt:
        for nums_num in nums:
            if len(nums_num) == k:
                cnt += 1

    # 세로방향 확인
    res_col = []
    for idx in range(n):
        strs = ''
        for nums in board:
            strs = strs + nums[idx]
        res_col.append(strs)
    res_col_spt = list(map(lambda x: x.split('0'), res_col))

    for nums in res_col_spt:
        for nums_num in nums:
            if len(nums_num) == k:
                cnt += 1
    
    print(f'#{test_case+1} {cnt}')
