import sys
input = sys.stdin.readline

N, r, c = map(int, input().split()) # r, c는 0부터 시작

n = 2**N # 한 변의 길이

# 몇사분면에 있는지 확인
# 중간 : n//2-1 ~ n//2

# 가장 작은 네 칸에서 값 구하기
def calc(idx):
    if idx == (0, 0):
        return 0
    elif idx == (0, 1):
        return 1
    elif idx == (1, 0):
        return 2
    else:
        return 3

def recursion(idx, mid, cnt):
    if mid == 1:
        print(cnt+calc(idx))
        return
    if idx[0] < mid and idx[1] < mid: # 왼위
        recursion(idx, mid//2, cnt)
    elif idx[0] < mid and idx[1] >= mid: # 오위
        recursion((idx[0], idx[1]-mid), mid//2, cnt+mid**2)
    elif idx[0] >= mid and idx[1] < mid: # 왼아래
        recursion((idx[0]-mid, idx[1]), mid//2, cnt+mid**2*2)
    else: # 우아래
        recursion((idx[0]-mid, idx[1]-mid), mid//2, cnt+mid**2*3)


recursion((r, c), n//2, 0)