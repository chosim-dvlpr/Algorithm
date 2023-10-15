import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(T):
    N = int(input())
    a = input() # a는 문자열로 받기

    # new_list에 새로운 10개의 공간 할당 (카드는 0~9까지 10개)
    new_list = [0] * 10 # new_list == 카드의 빈도수

    for card in a: # 카드를 하나씩 분리
        new_list[int(card)] += 1 # new_list의 카드번호와 같은 인덱스에 1씩 더함

    maxs = new_list[0]
    max_num = 0 # 아래에서 비교할 인덱스 값. 첫번째번호인 0 부여

    for idx, num in enumerate(new_list):
        if maxs <= num: # new_list의 빈도수를 비교하여 최댓값 maxs 구함
            maxs = num
            if max_num < idx: # 만약 최댓값의 인덱스 번호가 max_num보다 클 경우 큰 값을 max_idx로 함
                max_num = idx

    print(f'#{tc+1}', max_num, maxs)


