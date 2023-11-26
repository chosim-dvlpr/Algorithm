def solution(elements):
    choose = 0
    sums_list = []
    while choose < len(elements):
        choose += 1
        for start in range(len(elements)):
            end = start + choose
            # 범위를 넘을 때
            if end > len(elements):
                sums = sum(elements[start:])
                sums += sum(elements[:end-len(elements)])
                sums_list.append(sums)            
                continue
            # 범위를 넘지 않을 때
            sums_list.append(sum(elements[start:end]))
    return len(set(sums_list))
