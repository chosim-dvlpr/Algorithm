import sys

T = int(sys.stdin.readline())

for test_case in range(T):
    R, S = sys.stdin.readline().split()
    new_word_list = []

    for idx in range(len(S)):
        word = S[idx:idx+1] * int(R)
        new_word_list.append(word)
    print(''.join(new_word_list))

'''
# 메모리 초과 오류
import sys
import copy

T = int(sys.stdin.readline())

for test_case in range(T):
    R, S = sys.stdin.readline().split()
    copy_S = copy.deepcopy(S)
    for i in range(len(S)): # i = 0 ~ len(S)-1
        word = S[i:i+1]
        mul_word = word * int(R)
        copy_S = copy_S.replace(word, mul_word)
    print(copy_S)
'''




