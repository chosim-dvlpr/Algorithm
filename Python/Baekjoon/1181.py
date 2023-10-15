'''
알파벳 소문자로 이루어진 n개의 단어를 다음 조건에 따라 정렬
1. 길이가 짧은 것부터
2. 사전 순으로
중복된 단어는 하나만 남기고 제거 => set 사용
'''
lst = []
for i in range(int(input())):
    st = input()
    a = (len(st), st)
    if a not in lst:
        lst.append(a)
lst.sort(key=lambda x:(x[0], x[1]))
for i in lst:
    print(i[1])