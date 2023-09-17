def solution(answers):
    answer = []
    pattern = {
        1: [1, 2, 3, 4, 5],
        2: [2, 1, 2, 3, 2, 4, 2, 5],
        3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }
    i = 0
    cnt = [0, 0, 0] # 맞춘 개수
    
    while i != len(answers):
        # 1번 학생
        idx_1 = i % len(pattern[1])
        # 2번 학생
        idx_2 = i % len(pattern[2])
        # 3번 학생
        idx_3 = i % len(pattern[3])
        
        idx = answers[i]
        if idx == pattern[1][idx_1]:
            cnt[0] += 1
        if idx == pattern[2][idx_2]:
            cnt[1] += 1
        if idx == pattern[3][idx_3]:
            cnt[2] += 1
        
        i += 1
        
    mx = max(cnt) # cnt 리스트의 최대값
    
    for i, n in enumerate(cnt):
        if mx == n: # 가장 높은 점수를 가진 사람만 배열에 추가
            answer.append(i+1)
    
    
    return answer
