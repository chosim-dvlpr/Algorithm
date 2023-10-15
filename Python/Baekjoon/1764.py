'''
# 리스트 사용

N, M = map(int, input().split(' '))

set_list_N = []
set_list_M = []

for num in range(N):
    name_N = input()
    set_list_N.append(name_N)

for num in range(M):
    name_M = input()
    set_list_M.append(name_M)

new_list = list(set(set_list_N) & set(set_list_M))
new_list.sort()
print(len(new_list))
print(*new_list, sep='\n')




# 딕셔너리 사용

N, M = map(int, input().split(' '))
dict_N = {}
list_a = []

for num in range(N):
    name_N = input()
    dict_N[name_N] = 1

for num in range(M):
    name_M = input()
    if name_M in dict_N:
        list_a.append(name_M)
list_a.sort()

print(len(list_a))
print(*list_a, sep='\n')
'''
import sys
n, m = map(int, input().split())
nameList = sys.stdin.read().splitlines()
hearset = set(nameList[:n])
seeset = set(nameList[n:])
ret = list(hearset & seeset)
ret.sort()
print(len(ret))
for i in ret:
    print(i)