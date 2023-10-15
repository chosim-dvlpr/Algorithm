import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(T):
    N = int(input())

    # 모든 정류장은 1000개까지 있고, 각 번호가 부여되어 있음
    # => blank 리스트에 정차하는 정류장 각각 +1 하도록 코드를 짬
    blank = [0] * 1001

    for num in range(N):
        type, A, B = map(int, input().split()) # 1 : 일반, 2 : 급행, 3 : 광역
        res = 0 # 최대값 구하기 위한 변수

        # A와 B는 항상 정차하는 곳이기 때문에 1을 따로 더함
        # => 아래 for문의 범위에서 A, B는 제외
        blank[A] += 1
        blank[B] += 1

        # 범위 나누기
        if type != 3: # 일반 / 급행 버스일 때
            for idx in range(A+type, B, type):
                # 짝수 + 짝수 = 짝수, 짝수 + 홀수 = 홀수, 홀수 + 홀수 = 짝수 이용
                # type 1일때, 범위는 A+1 ~ B-1
                # type 2일때, 범위는 A+2 ~ B-1, 2 간격
                # A가 짝수면, 짝수 + 2 = 짝수
                # A가 홀수면, 홀수 + 2 = 짝수
                blank[idx] += 1
        else: # 광역 버스일 때
            for idx in range(A+1, B):
                if A % 2 == 0:              # A가 짝수일 때
                    if idx % 4 == 0:        # idx가 4의 배수일 때
                        blank[idx] += 1
                else:                                       # A가 홀수일 때
                    if (idx % 3 == 0) and (idx % 10 != 0):  # idx가 3의 배수O, 10의 배수X일 때
                        blank[idx] += 1

        for i in blank:
            if res < i:
                res = i

    print(f'#{tc + 1} {res}')



    '''
    첫 번째 작성했던 코드
    
        if type == 1: # 일반 버스
            for idx in range(A+1, B):
                blank[idx] += 1

        elif type == 2: # 급행 버스
            if A % 2 == 0: # A가 짝수일때
                for idx in range(A+1, B):
                    if idx % 2 == 0: # 범위 내의 인덱스 번호가 짝수이면
                        blank[idx] += 1

            else: # A가 홀수일 때
                for idx in range(A+1, B,):
                    if idx % 2 == 1:
                        blank[idx] += 1

        else: # 광역 급행 버스
            if A % 2 == 0: # A가 짝수일 때
                for idx in range(A+1, B):
                    if idx % 4 == 0:
                        blank[idx] += 1

            else: # A가 홀수일 때
                for idx in range(A+1, B):
                    if (idx % 3 == 0) and (idx % 10 != 0):
                        blank[idx] += 1
        '''



