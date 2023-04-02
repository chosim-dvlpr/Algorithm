'''
1개 이상의 수를 선택하여 합계가 k가 되는 경우의 수 구하기
n : lst의 길이
lst : 주어지는 수
k : 구해야 하는 합계
cnt : 총합이 구해야 하는 합계 k가 되는 부분집합의 수
'''

def func(num, sums):
    global cnt
    if sums > k:    # 합계가 구해야 하는 값 k보다 크면 종료
        return

    if num == n:        # 인덱스 번호가 lst의 길이와 같아지면 종료
        if sums == k:
            cnt += 1
        return

    func(num+1, sums+lst[num])
    func(num+1, sums)


for tc in range(1, int(input())+1):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0

    func(0, 0)  # (0, 0) : 시작 인덱스, 현재 합계

    print(f'#{tc} {cnt}')