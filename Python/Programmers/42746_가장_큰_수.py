
# numbers의 원소의 크기는 1000 이하
# 원소를 문자열로 바꿔 3번 반복 (*3)
# 반복한 수의 문자열을 인덱스 = 0부터 차례로 sort
# 00, 000이 나올 수 있으므로 int 조건을 걸어 0으로 처리해줌

def solution(numbers):
    newList = list(map(str, numbers))
    newList.sort(key=lambda x:x*3, reverse=True)
    return str(int(''.join(newList)))
