import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
mnDP = arr
mxDP = arr

for _ in range(n-1):
    inputArr = list(map(int, input().split()))
    mxDP = [inputArr[0] + max(mxDP[0], mxDP[1]), inputArr[1] + max(mxDP), inputArr[2] + max(mxDP[1], mxDP[2])]
    mnDP = [inputArr[0] + min(mnDP[0], mnDP[1]), inputArr[1] + min(mnDP), inputArr[2] + min(mnDP[1], mnDP[2])]

print(max(mxDP), min(mnDP))
