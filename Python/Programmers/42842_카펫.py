def solution(brown, yellow):
    answer = []
    for i in range(1, brown+1):
        temp = i * 2
        y_row = (brown - temp) // 2
        if y_row * (i-2) == yellow:
            if i > y_row+2:
                answer.append(i)
                answer.append(y_row+2)
            else:
                answer.append(y_row+2)
                answer.append(i)
            break
    return answer
