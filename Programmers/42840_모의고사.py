def solution(answers):
    answer = []
    pattern = {
        1: [1, 2, 3, 4, 5],
        2: [2, 1, 2, 3, 2, 4, 2, 5],
        3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }
    i = 0
    cnt = [0] * 4

    while i != len(answers):
        # 1번 학생
        idx_1 = i % len(pattern[1]) - 1
        # 2번 학생
        idx_2 = i % len(pattern[2]) - 1
        # 3번 학생
        idx_3 = i % len(pattern[3]) - 1
        
        for n in range(1, 4):
            if answers[i] == pattern[n][i]:
                cnt[n] += 1
        print(cnt)
        i += 1
    
    # 맞춘 개수 비교
    
        
    
    
    
    return answer
