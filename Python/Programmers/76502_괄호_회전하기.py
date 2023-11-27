# x : 0 ~ s-1

def check(start, end, st, n):
    stack = []
    flag = 0
    for i in range(start, end):
        s = st[i%n]
        # 열린 괄호일 때
        if s in ['[', '{', '(']:
            stack.append(s)
        # 닫힌 괄호일 때
        else:
            if not stack:
                return 0
            else:
                temp = stack.pop()
                if s == ']' and temp != '[':
                    flag = 1
                    break
                elif s == '}' and temp != '{':
                    flag = 1
                    break
                elif s == ')' and temp != '(':
                    flag = 1
                    break
    if flag or stack:
        return 0
    else:
        return 1

def solution(s):
    stack = []
    # 왼쪽으로 x칸만큼 회전 = 인덱스 시작점 +1
    x = 0
    n = len(s)
    cnt = 0
    
    while 1:
        if x == n:
            return cnt
        start = x
        end = x + n
        cnt += check(start, end, s, n)
        x += 1
