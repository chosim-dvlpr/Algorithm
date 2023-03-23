st = list(input())
stack = []
res = []

icp = {'*':2, '/':2, '+':1, '-':1, '(':3}
isp = {'*':2, '/':2, '+':1, '-':1, '(':0}

for word in st:
    if word.isalpha():  # 문자이면 res에 추가
        res.append(word)
    else:
        if word == '(':
            stack.append(word)  # 열린 괄호는 스택에 추가
        elif word == ')':       # 닫힌 괄호는 스택을 빼냄
            while stack:
                a = stack.pop()
                if a != '(':
                    res.append(a)
                else:
                    break
        else:   # 연산자일 때
            while stack and icp[word] <= isp[stack[-1]]:
            # 새로 들어오는 연산자의 우선순위가 스택 마지막의 연산자보다 높지 않을 때
                res.append(stack.pop())
            stack.append(word)

while stack:
    res.append(stack.pop())
print(''.join(res))