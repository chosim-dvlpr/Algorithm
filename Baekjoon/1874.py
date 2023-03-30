'''
스택 => LIFO
push =>순서는 항상 오름차순
1~n까지의 수를 오름차순으로 스택에 넣음 ==수열
이 수열이 주어진 수들과 같도록 연산자 출력
+ : push
- : pop

* 수를 무조건 push 후 pop 가능 - 생략 가능 (시간 줄이기)
=> 반대로 생각해보기
- 주어진 수를 정렬하여 오름차순으로 만들기
- 그 결과 나오는 push, pop의 값을 서로 바꾸고 (-는 +로, +는 -로) 뒤집기
'''

import sys

n = int(sys.stdin.readline())
num_list = list(map(int, range(1, n+1)))[::-1]
lst = [int(sys.stdin.readline()) for _ in range(n)][::-1]
stack = []
res = []
pushpop = []

for i in lst:
    pushpop.append('+') # 모든 값은 push됨
    if i == n:  # i가 최고값일 때
        res.append(i)
        pushpop.append('-')
    while res and res[-1]-1 != i: # res에 값이 들어있고 res의 가장 마지막 값에 1을 뺀 값이 i와 같다면
        res.append(i)
        pushpop.append('-')
if not stack or res != lst:
    print('NO')
else:
    print('YES')

