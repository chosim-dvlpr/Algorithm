# Baekjoon 4673


def fn_d(n):
    n_list = list(map(int, str(n)))
    gen = sum(n_list) + n
    return n, gen  # n은 gen의 제너레이터 - n이 없으면 셀프넘버


def is_selfnumber(n):
    n_list = list(map(int, range(1, fn_d(n)[1] + 1)))  # gen까지의 정수 리스트
    new_list = []  # 제너레이터 n이 있는 숫자들을 넣기 위한 빈 리스트
    for num in range(1, n + 1):  # num == 1~n
        new_list.append(fn_d(num)[1])  # new_list에 num의 gen을 추가
        if new_list[num - 1] in n_list:
            n_list.remove(new_list[num - 1])

    return n_list


print(*is_selfnumber(10000),sep='\n') # 리스트를 한 줄에 하나씩 출력