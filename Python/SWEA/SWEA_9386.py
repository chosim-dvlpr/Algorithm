import sys
sys.stdin = open("input.txt", "r")

T = int(input())

'''
for tc in range(T):
    N = int(input())
    arr = input()
    cnt = 0
    lst = []

    for word in arr:
        if word == '0':
            cnt = 0
        else:
            cnt += 1
            lst.append(cnt)

    maxs = lst[0]
    for num in lst:
        if maxs < num:
            maxs = num
    print(f'#{tc+1} {maxs}')
'''

# 더 짧은 풀이
for tc in range(T):
    N = int(input())
    lst = list(map(int, input()))
    ans = cnt = 0

    for i in range(N):
        if lst[i] == 0: # 0을 만날경우 cnt 초기화
            cnt = 0
        else:
            cnt += 1
            if ans < cnt: # 최대값 구하기
                ans = cnt

    print(f'#{tc+1} {ans}')
