import string

N = input()
alpha = list(string.ascii_lowercase)
lst = []

# 처음 등장하는 위치를 인덱스 번호로 변경
for idx in range(len(alpha)):
    a = N.find(alpha[idx])
    lst.append(str(a))
print(' '.join(lst))
