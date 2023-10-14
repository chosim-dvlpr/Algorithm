def solution(input_string):
    answer = ''
    res = [] # 외톨이 알파벳 담을 리스트

    length = len(input_string) # 11개
    
    # input_string : 'edeaaabbccd'
    
    # 연속으로 같은 문자열 확인
    def check_string(idx):
        rng = []
        i = 1
        while 1:
            if idx + i >= length:
                break

            if input_string[idx+i] == input_string[idx]:
                rng.append(idx+i)                
                i += 1
                
            else:
                break

        if rng:
            rng = [idx] + rng
            print('rng : ', rng)
            return rng
        else:
            return [idx]
    # s : 2, end : 3
    def find_string(start, end):
        rng = end - start + 1 # 2
        i = end + 1           # 4
        while 1:
            # 같은 문자열을 찾지 못했을 때
            if i >= length - (end - start):
                return False
            
            # 주어진 문자열과 같은 문자열이 있을 때
            # input_string[2:4] == input_string[4:6]
            if input_string[start:end+1] == input_string[i:i+rng]:
                # 같은 문자열의 다음 인덱스가 범위 안에 있고, 주어진 문자와 다른 문자일 때
                if i + rng < length and input_string[i] != input_string[i+rng]:
                    return True
                # 같은 문자열이 가장 마지막에 위치한 문자열일 때
                if i + rng + 1 >= length:
                    return True
            i += rng # i는 4 + 2 = 6
        

    
    
    
    idx = 0
    
    while 1:
        # 마지막 인덱스일 때
        if idx >= length-1:
            break
        a = check_string(idx)

        if input_string[a[0]:a[-1]+1] not in res:
            r = find_string(a[0], a[-1])

            if r: # 같은 문자열이 있을 때
                res.append(input_string[a[0]:a[0]+1])
        idx += a[-1] - a[0] + 1
    if res:
        res.sort()
        answer = ''.join(res)    
    else:
        answer = "N"
    return answer
            
