'''
문자열의 (), []괄호의 쌍이 맞아야 함 ->스택
문장의 마지막은 온점 .으로 끝남

닫힌 괄호가 나온다면 pop ->종류가 맞는 열린 괄호가 나오면 yes
=>스택에 남는 괄호가 없어야 함
중간에 .이 나오면 no
'''


while 1:
    st = input()
    stack = []

    if st == '.':
        break

    flag = 1
    if st[-1] != '.':
        flag = 0
    else:
        for s in range(len(st)-1):
            if st[s] == '.':
                flag = 0
                break
            if not st[s].isdigit():
                if st[s] == '(' or st[s] == '[':
                        stack.append(st[s])
                elif st[s] == ')' or st[s] == ']': 
                    if not stack:
                        flag = 0
                        break
                    a = stack.pop()
                    if st[s] == ')':
                        if a != '(':
                            flag = 0
                            break
                    else:
                        if a != '[':
                            flag = 0
                            break
                            
    if flag and not stack:
        res = 'yes'
    else:
        res = 'no'

    print(res)
    
