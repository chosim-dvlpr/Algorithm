import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(T):
    N = int(input())
    blank_list = [0] * 5001 # 0 리스트 생성

    for i in range(N):
        A, B = map(int, input().split()) # 범위 A, B 값 입력받음
        for idx in range(A, B+1):        # A이상, B이하이므로 범위는 range(A, B+1)
            blank_list[idx] += 1         # 해당 범위에 해당하는 blank_list 값에 1씩 추가

    P = int(input())
    new_list = []

    for i in range(P):
        C = int(input()) # 출력할 정류소 번호
        new_list.append(blank_list[C]) # blank_list의 인덱스가 C인 값을 새로운 리스트에 넣음
    print(f'#{tc+1}', *new_list)



