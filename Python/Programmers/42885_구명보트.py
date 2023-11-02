# 가장 무거운 사람 + 가장 가벼운 사람 한 배에 태우는게 가장 이득
# people 정렬 후 0번째와 -1번째 사람을 한 배에 태움
# limit 넘어간다면 무거운 사람을 먼저 pop

from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    
    while len(people) > 1:
        if people[0] + people[-1] <= limit:
            people.popleft()
        answer += 1
        people.pop()
    
    if people:
        answer += 1
    return answer
