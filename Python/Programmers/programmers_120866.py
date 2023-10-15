# board : 지뢰매설된 지도, n*n배열
# 지뢰 매설 : 1
# 안전한 지역의 칸 수를 반환하여라


def solution(board):
    L = len(board)
    tnt = []
    for i in range(L): # 세로줄 확인
        for j in range(L): # 가로줄 확인
            if board[i][j] == 1: # 폭탄이 있는 인덱스 번호 i, j
                tnt.append([i, j]) # 인덱스 번호 통째로 새로운 리스트에 저장 (ex. tnt = [[1,1], [2,3]] )

    di = [0, 1, 0, -1, 1, 1, -1, -1] # 오른쪽, 아래, 왼쪽, 위쪽, 오른쪽 아래, 왼쪽아래, 왼쪽위, 오른쪽위 순서로 탐색
    dj = [1, 0, -1, 0, 1, -1, -1, 1] 

    for lst in tnt: # tnt의 인덱스 번호 순서로 탐색
        for k in range(len(di)): # 8방향 탐색 (==len(di))
            ni, nj = lst[0]+di[k], lst[1]+dj[k] # di, dj만큼 이동후의 좌표
            if 0<=ni<L and 0<=nj<L: # 범위 밖으로 나가지 않도록 조건 걸어줌
                board[ni][nj] += 1

    # board에서 0이 아닌 값 찾아 카운트
    cnt = 0
    for idx in range(L):
        for j in range(L):
            if board[idx][j] == 0:
                cnt += 1

    return cnt

board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]

print(solution(board))
