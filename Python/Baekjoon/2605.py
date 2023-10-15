'''
n : 학생 수
lst : 학생들이 뽑은 번호
'''

n = int(input())
lst = list(map(int, input().split()))
temp = []
num = 1
for i in lst:
    temp.insert(i, num)
    num += 1
print(*temp[::-1])