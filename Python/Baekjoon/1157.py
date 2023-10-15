import sys

# 문자를 받아옴 (대소문자 상관없이, 불필요한 공백 제거)
words = sys.stdin.readline().casefold().strip()
count_dict = {}

for word in words:
    if word not in count_dict:
        count_dict[word] = words.count(word)
        # 시간 초과 방지 위해 조건 제시
        # count_dict에 해당 알파벳이 없는 경우만 확인하도록 함

# key, value값을 튜플로 받는 리스트 생성 [('a' : 3), ..]
items_list = [x for x in count_dict.items()]

# items_list 속 튜플 인덱스번호 1로 정렬 = 카운트 한 숫자
items_list.sort(key=lambda x:x[1])

# 글자수가 한개일때 최대 빈도수인 문자는 word(=입력받은 문자)
if len(items_list) < 2:
    print(word.upper())
else:
    if items_list[-1][1] == items_list[-2][1]:
        print('?')
        # 정렬한 리스트의 가장 마지막 요소와 끝에서 두번째 요소 비교
    else:
        print(items_list[-1][0].upper())
