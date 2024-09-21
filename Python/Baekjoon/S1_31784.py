import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = input().strip()
arr_num = [ord(word)%65 for word in arr]
idx = 0
end_idx = n-1

while k != 0 and idx < n-1:
    if arr_num[idx] == 0:
        idx += 1
        continue

    diff = 26 - arr_num[idx]

    if k >= diff:
        k -= diff
        arr_num[idx] = 0
    else:
        next_idx = idx + 1
        while next_idx < end_idx:
            next_diff = 26 - arr_num[next_idx]
            if k >= next_diff:
                k -= next_diff
                arr_num[next_idx] = 0
            next_idx += 1
        if k:
            arr_num[end_idx] = (arr_num[end_idx] + k) % 26
            k = 0
    idx += 1
if k:
    arr_num[end_idx] = (arr_num[end_idx] + k) % 26

for num in arr_num:
    print(chr(num+65), end="")