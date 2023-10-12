def solution(input_string):
    answer = 0
    find_alpha = '' # 찾고자 하는 문자
    n = len(input_string)
    res = [] # 외톨이 알파벳을 담을 리스트
    idx = 0
    
    # 다음 문자가 같은 문자인지 확인
    def if_same(idx, word):
        length = 0
        
        for i in range(idx, n):
            if input_string[i] == word:
                length += 1
            else:
                return length
    
    # 문자열 전체 확인
    def check(i):
        
        
        while 1:
            # 뒤에서 두번째까지 확인
            if i == n-1:
                break
                
            # i+1번째부터 input_string[i]와 같은 문자가 있다면 개수 반환
            length = if_same(i+1, input_string[i]) 

            st = input_string[i:i+length+1] # 반복되는 (되지 않는) 기준 문자열
            
            # 기준 문자열의 다음 인덱스부터 끝까지 순회
            for j in range(i+length+1, n-length-i):
                find_st = input_string[j:j+length+1] # 기준 문자열과 같은 문자열이 있는지 비교
                print("find_st", find_st, st, j, j+length)
                
                if find_st == st:
                    print("같음")
                    if find_st not in res:
                        res.append(find_st)
                        print("res : ", res)
                    check(i+length+1)
            return
                
            # if st not in res:
            #     res.append(st)
                
    check(0)     
    answer = ''.join(set(res))
    
    
    return answer
