'''
n : 수열의 길이
arr : 수열
수열이 1씩 증가하거나 작아지는 연속된 구간 찾아 최댓값 출력
'''

n = int(input())
arr = list(map(int, input().split()))
cnt_lst = []    # cnt 값을 저장할 리스트
sm = 1  # 같은 숫자가 나올때

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    cnt = 2
    if arr[0] < arr[1]:
        d = 1
    elif arr[0] > arr[1]:
        d = -1
    else:
        d = 0
    for i in range(2, n):
        if arr[i-1] < arr[i]:   # 증가하는 경우
            if d >= 0:
                cnt += 1
                cnt_lst.append(cnt)
                d = 1
                sm = 1
            else:
                cnt = sm + 1
                d = 1
                cnt_lst.append(cnt)
                sm = 1
        elif arr[i-1] > arr[i]: # 감소하는 경우
            if d > 0:
                cnt = sm + 1
                d = -1
                cnt_lst.append(cnt)
                sm = 1
            else:
                cnt += 1
                cnt_lst.append(cnt)
                d = -1
                sm = 1
        else:                   # 일정한 경우
            sm += 1
            cnt += 1
            cnt_lst.append(cnt)
    print(max(cnt_lst))
