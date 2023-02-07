import sys
sys.stdin = open("input.txt", "r")

# 함수 사용하여 구현
T = int(input())

def bin_search(P, Pi):
    start = 1 # 시작 페이지
    end = P   # 종료 페이지
    cnt = 1
    a = list(map(int, range(0, P))) # 총 페이지 리스트

    while start <= end: # 시작점이 종료지점보다 같거나 작을때까지만 반복
        middle = int((start + end) / 2) # 중간값
        if a[middle] == Pi: # 총 페이지의 middle번째 값이 찾는 쪽 번호가 Pi와 같아지면
            return cnt
        elif a[middle] > Pi: # 찾는 번호가 페이지의 중앙값보다 작다면
            end = middle     # 찾는 범위의 종료지점을 중앙값으로 둠
        elif a[middle] < Pi: # 찾는 번호가 페이지의 중앙값보다 크다면
            start = middle   # 찾는 범위의 시작지점을 중앙값으로 둠
        cnt += 1 # 횟수 카운트 +1

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split()) # P : 전체 쪽수, Pa, Pb : 각각 찾아야 하는 페이지

    # a, b의 카운트 횟수(=찾는쪽 번호와 중앙값이 같아질때까지 반복한 횟수)
    a_cnt = bin_search(P, Pa)
    b_cnt = bin_search(P, Pb)

    # a, b의 카운트 횟수 비교
    # 여기서 카운트가 작으면 이김
    if a_cnt > b_cnt:
        res = 'B'
    elif a_cnt < b_cnt:
        res = 'A'
    else:
        res = 0

    print(f'#{tc} {res}')

    ''' 
    # 함수 사용하지 않고 구현
    
    while a_start <= a_end:
        a_middle = int((a_start + a_end) / 2)
        if a[a_middle-1] == Pa:
            break
        elif a[a_middle-1] > Pa:
            a_end = a_middle
        elif a[a_middle-1] < Pa:
            a_start = a_middle
        a_cnt += 1


    while b_start <= b_end:
        b_middle = int((b_start + b_end) / 2)
        if a[b_middle-1] == Pb:
            break
        elif a[b_middle-1] > Pb:
            b_end = b_middle
        elif a[b_middle-1] < Pb:
            b_start = b_middle
        b_cnt += 1

    if a_cnt > b_cnt:
        res = 'B'
    elif a_cnt < b_cnt:
        res = 'A'
    else:
        res = 0

    print(f'#{tc} {res}')
    '''


