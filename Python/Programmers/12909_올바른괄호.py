from collections import deque

def solution(s):
    answer = True
    stack = deque([])
    for word in s:
        if word == '(':
            stack.append(word)
        else:
            if stack:
                stack.pop()
            else:
                answer = False
                break
    if stack:
        answer = False
    return answer
