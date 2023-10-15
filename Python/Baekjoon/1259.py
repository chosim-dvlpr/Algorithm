import sys

while 1:
    N = sys.stdin.readline().strip()
    if N == '0':
        break
    else:
        new_list = []
        for word in N:
            new_list.append(word)
        new_list.reverse()

        if ''.join(new_list) == N:
            print('yes')
            continue
        else:
            print('no')
            continue