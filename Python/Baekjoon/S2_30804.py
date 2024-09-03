import sys
input = sys.stdin.readline

n = int(input())
foods = list(map(int, input().split()))


if len(set(foods)) <= 2:
    print(len(foods))
elif len(set(foods)) == n:
    print(2)
else:
    s, e = 0, 0
    mx = 0
    cnt = {}

    while e < n:
        if foods[e] in cnt:
            cnt[foods[e]] += 1
        else:
            cnt[foods[e]] = 1
        
        while len(cnt) > 2:
            cnt[foods[s]] -= 1
            if cnt[foods[s]] <= 0:
                cnt.pop(foods[s])
            s += 1
        mx = max(mx, e - s + 1)
        e += 1
    print(mx)
