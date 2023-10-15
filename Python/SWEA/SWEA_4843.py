import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N_list = list(map(int, input().split()))

    # 선택 정렬 - 데이터 양이 적을 때 사용하면 좋음!
    for i in range(N): # list의 크기인 N만큼 반복
        minidx = i     # 최소 인덱스를 i라고 설정 = 맨 앞에 오는 값
        for j in range(i+1, N): # 최소 인덱스의 다음 인덱스부터 끝까지 데이터 확인
            if N_list[minidx] > N_list[j]: # 만약 최소 인덱스의 값보다 뒤 인덱스의 값이 더 작다면
                minidx = j                 # 최소 인덱스를 j로 바꿈
        N_list[i], N_list[minidx] = N_list[minidx], N_list[i] # 기존 최소인덱스와 새로운 최소인덱스를 교환

    # 결과 데이터 출력
    print(f'#{tc} ', end='')
    for idx in range(10): # 문제에서 10개까지 출력하라고 했으므로 10번 반복

        # 인덱스가 짝수일 때 정렬된 N_list의 뒤쪽 값 출력
        if idx % 2 == 0:
            print(N_list[-1-int(idx/2)], end=' ')
            # idx == 0, 2, 4, 6, 8이므로 2를 나눈 정수값을 -1에서 빼야함
            # idx/2 == 0, 1, 2, 3, 4
            # => (-1-int(idx/2)) == -1, -2, -3, -4, -5

        # 인덱스가 홀수일 때 정렬된 N_list의 앞쪽 값 출력
        else:
            print(N_list[int(idx/2)], end=' ')
            # idx == 1, 3, 5, 7, 9이므로 2를 나눈 정수값을 대입함
            # int(idx/2) == 0, 1, 3, 5, 7
    print()