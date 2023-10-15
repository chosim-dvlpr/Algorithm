import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(T):
    N = int(input())
    carrot_list = list(map(int, input().split()))
    res = cnt = 1 # 연속되지 않을 경우 초기값은 1이므로 변수에 1 부여

    # 입력값 순차 비교
    for idx in range(N-1):
        if carrot_list[idx+1] == carrot_list[idx] + 1: # 해당 인덱스 +1 값이 다음 인덱스 값과 같을 경우
            cnt += 1                                   # cnt에 1 더함
            if res <= cnt:
                res = cnt
        else:       # 연속되지 않는 값일 경우
            cnt = 1 # cnt를 1로 초기화
    print(f'#{tc+1} {res}')