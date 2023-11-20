from collections import deque

def solution(queue1, queue2):
    answer = -1
    limit = len(queue1) * 4
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sums1 = sum(queue1)
    sums2 = sum(queue2)
    
    while queue1 and queue2:
        answer += 1
        # 합 일치 시 종료
        if sums1 == sums2:
            return answer
        # 나올 수 있는 경우의 수를 넘어가면 종료
        if answer > limit:
            return -1
        # sums 대소비교
        if sums1 > sums2:
            element = queue1.popleft()
            queue2.append(element)
            sums1 -= element
            sums2 += element
        else: 
            element = queue2.popleft()
            queue1.append(element)
            sums1 += element
            sums2 -= element
    return -1
