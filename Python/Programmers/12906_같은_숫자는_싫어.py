def solution(arr):
    answer = []
    for a in arr:
        if not answer:
            answer.append(a)
        elif answer and answer[-1] != a:
            answer.append(a)
    return answer
