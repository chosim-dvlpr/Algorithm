import sys
stack = []
for i in range(int(sys.stdin.readline())):
    n = int(input())
    if n != 0:
        stack.append(n)
    else:
        stack.pop()
print(sum(stack))