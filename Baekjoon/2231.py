import sys

N = int(sys.stdin.readline())
x = 1

while 1:
    x_list = list(int(i) for i in str(x))
    if x + sum(x_list) == N:
        print(x)
        break
    else:
        if x >= N:
            print(0)
            break
        else:
            x += 1
        


'''
N = 123
N_list = list(int(x) for x in str(N))
print(N_list)
'''