import sys

stack = []
for _ in range(int(sys.stdin.readline())):
    lst = list(map(str, sys.stdin.readline().split()))
    # print(lst)
    if lst[0] == 'push':
        stack.append(lst[1])
    elif lst[0] == 'pop':
        if stack:
            print(stack.pop(-1))
        else:
            print(-1)
    elif lst[0] == 'size':
        print(len(stack))
    elif lst[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)