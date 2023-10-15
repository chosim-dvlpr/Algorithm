for i in range(1,int(input())+1):
    N, M = map(int, input().split())
    aj = list(map(int, input().split()))
    bj = list(map(int, input().split()))
    
    if len(aj) > len(bj):
        aj, bj = bj, aj # a를 b로, b를 a로 바꿈
    
    new_list = []
    for k in range(len(bj)-len(aj)+1):
        sums = 0
        for z in range(len(aj)):
            sums += aj[z] * bj[z+k]
        new_list.append(sums)
    maxs = max(new_list)
    print(f'#{i} {maxs}')
