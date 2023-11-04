def solution(rank, attendance):
    answer = 0
    lst = [[] for _ in range(len(rank))]
    
    for i, r in enumerate(rank):
        lst[i] = [r, i, attendance[i]]
    lst.sort(key=lambda x:x[0])
    
    rnk = [0, 0, 0]
    cnt = 0
    for i in lst:
        if i[2] == True:
            rnk[cnt] = i[1]
            cnt += 1
            if cnt == 3:
                break
    return 10000 * rnk[0] + 100 * rnk[1] + rnk[2]
