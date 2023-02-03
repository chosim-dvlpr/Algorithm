T = int(input())

for tc in range(T):
    word = input()
    new_word = word[::-1]
    if word == new_word:
        res = 1
    else:
        res = 0
    print(f'#{tc+1} {res}')