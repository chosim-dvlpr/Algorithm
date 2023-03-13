'''
VPS : ()
VPS 조건
1. 여는 괄호 개수 == 닫는 괄호 개수
2. 여는 괄호와 닫는 괄호가 쌍을 이루어야
'''

for _ in range(int(input())):
    st = list(map(str, input()))
    stack = []
    res = 'YES'
    for word in st:
        if word == '(': # 여는 괄호일 때 : stack에 추가
            stack.append(word)
        else:           # 닫는 괄호일 때 : stack 확인
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                res = 'NO'
                break
    if len(stack) != 0:
        res = 'NO'

    print(res)