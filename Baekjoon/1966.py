'''
가장 앞에 있는 문서의 중요도 확인
나머지 문서 중 중요도가 높은 문서가 하나라도 있으면
=> 이 문서 인쇄X, Queue의 가장 뒤에 재배치
중요도 높은 문서가 하나도 없으면
=> 이 문서 인쇄

문서가 몇 번째로 인쇄되는지 출력하기
'''

for _ in range(int(input())):   # 테스트 케이스
    # n : 문서의 개수, m : 몇번째로 인쇄되었는지 찾아야할 문서의 번호
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))   # n개 문서의 중요도
    identify = [0]*n
    identify[m] = 1

    i = 1
    cnt = 0
    if n == 1:
        res = 1
    else:
        while 1:
            if len(lst) == 1:
                res = cnt + 1
                break
            if lst[0] < lst[i]:
                lst.append(lst.pop(0))
                identify.append(identify.pop(0))
                i = 1
                continue
            i += 1
            if i == len(lst):
                if identify[0] == 1:
                    res = cnt + 1
                    break
                else:
                    lst.pop(0)
                    identify.pop(0)
                    cnt += 1
                    i = 1
                    continue
    print(res)
