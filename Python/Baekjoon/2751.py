import sys
lst = []
for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    lst.append(num)

lst.sort(key=lambda x:x)
for i in lst:
    print(i)