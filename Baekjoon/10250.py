import sys
sys.stdin = open("input.txt", "r")

# n번째 손님에게 배정할 방 번호를 구하여라
# 같은 호수면 낮은 층 선호
# 각 호수당 차이는 1
# 높이는 상관없음

for tc in range(int(input())):
    h, w, n = map(int, input().split()) # h : 층, w : 호수, n : n번째 손님

    # 층수 : n%h
    # 호수 : n//h

    # 호수
    x = n//h+1

    # 층수
    YY = n%h
    if YY == 0:
        YY = h
        x -= 1

    if x < 10:
        XX = '0'+str(x)
    else:
        XX = str(x)

    print(f'{YY}{XX}')

