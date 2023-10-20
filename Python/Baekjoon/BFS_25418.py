# 연산에 따라 a를 k로 변경
# 연산 1 : 정수 a에 +1
# 연산 2 : a * 2
# a를 k로 만들기 위한 최소 연산 횟수는?

a, k = map(int, input().split())
cnt = 987654321 # 연산 횟수

def calc(a, idx):
    global cnt
    # print("a : ", a)
    if a == k:
        if cnt > idx:
            cnt = idx
        return

    elif a > k:
        return
    
    else:
        calc(a * 2, idx+1)
        calc(a + 1, idx+1)
        # # print("cnt : ", cnt)
        # for i in range(2):
        #     # print("i : ", i)
        #     if i:
        #         calc(a * 2, idx+1)
        #     else:
        #         calc(a + 1, idx+1)

calc(a, 0)
print(cnt)
