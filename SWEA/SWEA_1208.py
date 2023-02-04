def get_max_idx():
    max_value = 0 # 처음에는 최대값을 가장 작은 값으로 설정
    max_idx = -1 # 초기값은 유효하지 않는 값으로 설정
    for i in range(len(boxes)):
        if boxes[i] > max_value:
            max_value = boxes[i]
            max_idx = i
    return max_idx

def get_min_idx():
    min_value = 987654321
    min_idx = -1
    for i in range(len(boxes)):
        if boxes[i] < min_value:
            min_value = boxes[i]
            min_idx = i
    return  min_idx


for tc in range(10):
    n = int(input())
    boxes = list(map(int, input().split()))
    for i in range(n): # 덤프 횟수만큼 반복
        boxes[get_max_idx()] -= 1 # boxes에서 가장 높은 칸의 값을 가져옴 => 1을 빼기
        boxes[get_min_idx()] += 1

    res = boxes[get_max_idx()] - boxes[get_min_idx()] # 평탄화가 끝난 뒤의 결과
    print(f'#{tc + 1} {res}')
