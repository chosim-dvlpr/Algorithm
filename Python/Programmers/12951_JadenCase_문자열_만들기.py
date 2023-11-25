# 첫 문자가 대문자, 나머지는 소문자
# 첫 문자가 알파벳이 아니면 모두 소문자로 쓰기
# s를 JadenCase로 바꾼 문자열을 리턴하기

def solution(s):
    answer = []
    for st in s.split(' '):
        answer.append(st.capitalize())
    return ' '.join(answer)
    
