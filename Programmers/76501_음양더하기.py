def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(absolutes)):
        if signs[i]: # 양수일 때
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer
