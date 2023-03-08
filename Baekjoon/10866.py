
import sys

def push(x, y):
    global lst
    if x == 'push_front':   # lst 앞에 값 넣기
        lst = [y] + lst
    elif x == 'push_back':  # lst 맨 뒤에 값 넣기
        lst.append(y)

def pops(x):
    global lst
    if not lst: # lst가 비어있다면
        return -1
    elif x == 'pop_front':  # 첫번째값 출력
        return lst.pop(0)
    else:                   # 마지막값 출력
        return lst.pop(-1)

def is_empty(): # lst가 비어있는지 확인
    if lst: # lst가 비어있지 않을 때
        return 0
    else:   # lst가 비어있다면
        return 1

def func(st):
    if len(lst) == 0:   # lst길이가 0일때
        return -1
    else:               # lst가
        if st == 'front':
            return lst[0]
        elif st == 'back':
            return lst[-1]

n = int(sys.stdin.readline())
lst = []

for _ in range(n):
    st = sys.stdin.readline().strip()
    if st[:3] == 'pop':
        print(pops(st))
    elif st == 'size':
        print(len(lst))
    elif st == 'empty':
        print(is_empty())
    elif st == 'front' or st == 'back':
        print(func(st))
    elif st[:3] == 'pus':
        x, y = map(str, st.split())
        push(x, int(y))


