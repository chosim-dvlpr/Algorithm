# SWEA 1966
# 오름차순 정렬하여 출력하기 (내장함수 사용x)

T = int(input())
for tc in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))

    new_list = [0] * 51 # 새로운 리스트에 51개의 공간 할당 (N은 50 이하) (0~50까지를 넣어주기 위해)
    temp = [0] * N # 최종적으로 정렬할 리스트 공간 할당

    for idx in range(N): # 해당되는 인덱스에 1씩 더함
        new_list[num_list[idx]] += 1
    for idx in range(1, len(new_list)): # 각 인덱스들의 누적합을 구해 기존 리스트에 넣어줌
        new_list[idx] += new_list[idx-1]
        # new_list = [1, 2, 2, 2, 3, 3, 3, 4, 5, 5 ..]

    for i in range(len(num_list)-1, -1, -1): # i는 N부터 1까지 순차적으로 작아짐
        # num_list[i]는 0 8 7 4 1 (거꾸로 나옴)
        new_list[num_list[i]] -= 1
        # new list [0]을 -1, [8]을 -1 .. => temp의 인덱스 범위가 나옴
        # new_list = [*0*, *1*, 2, 2, *2*, 3, 3, *3*, *4*, 5, ..]
        temp[new_list[num_list[i]]] = num_list[i] # temp[0]은 num_list의 [0]==0, temp[4]는 8 ..
    print(f'#{tc+1}', *temp)

