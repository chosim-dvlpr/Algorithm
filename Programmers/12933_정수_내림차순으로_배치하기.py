def solution(n):
    lst = list(map(str, str(n)))
    lst.sort(reverse=True)
    st = "".join(lst)
    # print(st)
    return int(st)
