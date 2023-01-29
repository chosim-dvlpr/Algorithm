N = list(map(str, input().split()))
N_word = ''.join(N)

if N_word == '12345678':
    print('ascending')
elif N_word == '87654321':
    print('descending')
else:
    print('mixed')
