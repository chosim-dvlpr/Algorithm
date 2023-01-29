import sys

N = int(sys.stdin.readline())

print(*(i+1 for i in range(N)), sep='\n')