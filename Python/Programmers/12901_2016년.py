def solution(a, b):
    # 윤년 => 2월 29일
    # 3, 5, 7, 8, 10, 12월 : 31일
    # 4, 6, 9, 11 : 30일
    
    total = 0
    if a == 1:
        total += 31
    elif a == 2:
        total += 29
    else:
        pass
    answer = ''
    return answer
