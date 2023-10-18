# 해시 함수 : 임의의 길이를 입력받아 고정된 길이의 출력 내보내는 함수
# 입력으로 들어오는 문자는 영문 소문자로 구성 (26개)
# a는 1, b는 2 .. 로 고유 번호 부여
# abba = 1,2,2,1
# 서로 다른 문자열이라도 동일한 해시 값을 가질 수 있음 (해시 충돌)
# 순서 바꾸게 되면 충돌 발생 (나쁜 해시 함수)
# 해결 : 항의 번호에 해당하는 만큼 특정 숫자를 거듭제곱해서 곱한 뒤 더하기
import sys

L = int(sys.stdin.readline()) # 문자열의 길이
st = list(map(str, sys.stdin.readline().strip()))

sum = 0
M = 1234567891

for i in range(len(st)):
    sum += (ord(st[i])-96) * (31 ** i)
print(sum % M)