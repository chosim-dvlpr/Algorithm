# L개의 소문자
# 최소 한 개의 모음
# 최소 두 개의 자음
# 알파벳이 증가하는 순서
# c개의 문자

import sys
input = sys.stdin.readline

l, c = map(int, input().split())
words = list(map(str, input().split()))
words.sort()
mo = ['a', 'e', 'i', 'o', 'u']
res = []

def bfs(word, idx, moCnt, jaCnt):
    if len(word) == l:
        if moCnt >= 1 and jaCnt >= 2:
            res.append(''.join(word))
        return

    for i in range(idx, c):
        word.append(words[i])
        if words[i] in mo:
            bfs(word, i+1, moCnt+1, jaCnt)
        else:
            bfs(word, i+1, moCnt, jaCnt+1)
        word.pop()


bfs([], 0, 0, 0)

res.sort()
for r in res:
    print(r)
