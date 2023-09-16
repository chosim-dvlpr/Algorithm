def solution(answers):
    answer = []
    pattern = {
        1: [1, 2, 3, 4, 5],
        2: [2, 1, 2, 3, 2, 4, 2, 5],
        3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }
    i = 0
    cnt = [[1, 0], [2, 0], [3, 0]] # 학생번호, 맞춘 개수

    while i != len(answers):
        # # 1번 학생
        # idx_1 = i % len(pattern[1]) - 1
        # # 2번 학생
        # idx_2 = i % len(pattern[2]) - 1
        # # 3번 학생
        # idx_3 = i % len(pattern[3]) - 1
        
        for n in range(1, 4):
            if len(pattern[n]) - 1 == i:
                idx = i
            else:
                idx = i % (len(pattern[n]) - 1)
            # print(i, idx, n)
            if answers[i] == pattern[n][idx]:
                cnt[n-1][1] += 1
        i += 1
    
    # 맞춘 개수 비교
    cnt.sort(key=lambda x: x[1], reverse=True)
    
    for idx in cnt:
        if idx[1] == 0:
            break
        answer.append(idx[0])
        
    
    
    
    return answer
