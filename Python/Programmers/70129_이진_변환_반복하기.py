def solution(s):
    answer = [0, 0] # 횟수, 제거한 0의 수

    while s != "1":
        answer[0] += 1
        new_string = ""
        for word in s:
            if word == "1":
                new_string += word
            else:
                answer[1] += 1
        s = bin(len(new_string))[2:]
    
    return answer
