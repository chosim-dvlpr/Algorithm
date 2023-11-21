# 출차 내역이 없다면 23:59 출차
# 누적 주차 시간 < 기본 시간 : 기본 요금
# 누적 주차 시간 > 기본 시간 : 기본 요금 + 단위시간 * 단위요금 (올림)
# 차량 번호 : string
# 차량 번호가 작은 자동차부터 청구 주차 요금 배열로 출력
# fees: [기본시간(분), 기본요금, 단위시간(분), 단위요금]
# records: 시각 차량번호 내역 (공백으로 분리)
# 시각 : HH:MM, 길이가 5

import math

# 시간 계산 -> 분으로 바꿈
def calcTime(start, end):
    start_h = int(start[:2])
    end_h = int(end[:2])
    
    start_m = int(start[3:])
    end_m = int(end[3:])
    
    if end_m >= start_m:
        mm = end_m - start_m
        hh = end_h - start_h
    else:
        mm = end_m - start_m + 60
        hh = end_h - start_h - 1
    return hh * 60 + mm
    
def solution(fees, records):
    dict = {} # 차량번호 : 시간 총합
    stack = [] # (출입시간, 차량번호)
    for r in records:
        record = list(map(str, r.split())) # [출입 시간, 차량번호, 출입]
        
        # IN : stack에 추가
        # OUT : stack에서 꺼내기
        if record[2] == 'IN':
            stack.append((record[0], record[1]))
            continue
        
        # 출차 : stack에서 꺼내기
        for s in stack:
            if s[1] == record[1]:
                total = calcTime(s[0], record[0])
                value = dict.get(record[1], -1)
                if value > -1:
                    dict[record[1]] += total
                else:
                    dict[record[1]] = total
                stack.remove(s)
                continue
    for s in stack:
        start = s[0]
        car = s[1]
        value = dict.get(car, -1)
        total = calcTime(start, '23:59')
        if value > -1:
            dict[car] += total
        else:
            dict[car] = total

    answer = []
    for key, value in dict.items():
        # 기본 시간보다 초과했을 때
        if value > fees[0]:
            total = fees[1] + fees[3] * math.ceil((value - fees[0]) / fees[2])
            answer.append((key, total))
        # 기본 시간 미만
        else:
            total = fees[1]
            answer.append((key, total))

    answer.sort(key=lambda x:x[0])
    
    result = []
    for a in answer:
        result.append(a[1])
    return result
