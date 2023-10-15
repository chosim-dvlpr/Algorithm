# 카드 : 1~ 99
# n : 4 ~ 10
# n장 중 k장 선택 (2~4)
# 가로로 정수를 만듦
# 정수의 개수는?

import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
cards = [input().strip() for _ in range(n)] # 보유한 카드

card_list = [] # 카드를 모아 만든 값을 넣을 리스트

def pick(st, i, picked):
    # [2] 인덱스가 뽑을 개수와 같아질 때
    if i == k:
        if st not in card_list: # 합친 문자열이 리스트에 없다면 추가
            card_list.append(st)
        return
    
    # [1]
    for idx in range(n): # picked 순회
        if not picked[idx]: # picked[idx]가 0일 때
            picked[idx] = 1 # 1로 바꿔주고 재귀
            pick(st + cards[idx], i+1, picked)
            picked[idx] = 0 # 0으로 초기화

picked = [0] * n
pick("", 0, picked)
print(len(card_list))
