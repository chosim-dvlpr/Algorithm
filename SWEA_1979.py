T = int(input())
for test_case in range(T):
    n, k = map(int, input().split())

    board = [input().split() for _ in range(n)]
    cnt = 0

    # 가로방향 확인
    res_row = []
    for lst in board:
        res_row.append(''.join(map(str, lst)))
    
    for nums in res_row:
        if '0'*k in nums:
            cnt += 1
        if '0'*(k+1) in nums:
            cnt -= 1
    # print(cnt)
        print(nums)
    
    # 세로방향 확인
    res_col = []
    for lst in board:
        res_col.append(''.join(map(str, lst)))
    # print(res_col)

    for nums in res_col:
        if '0'*k in nums:
            cnt += 1
        if '0'*(k+1) in nums:
            cnt -= 1
        
    # print(cnt)



    # 가로방향 확인 -> 빼기!
    for col in range(n): # 0일때
        for row in range(n): # 0~4 : 가로
            pass




            # print(board[col][row])
    # for lst in board:
    #     res.append(''.join(map(str, lst)))
    # print(res)

# print('111' in '111101101') # True


'''
a[col][row]
a[0][0] a[0][1] a[0][2]
a[1][0] a[1][1] a[1][2]
a[2][0] a[2][1] a[2][2]

'''

