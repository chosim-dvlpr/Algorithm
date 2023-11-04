# query 순회
# query의 짝수 인덱스 i : arr의 i 뒷부분 잘라냄
# query의 홀수 인덱스 i : arr의 i 앞부분을 잘라냄

def solution(arr, query):
    for i, q in enumerate(query):
        if i % 2: # 홀수일 때
            arr = arr[q:]
        else: # 짝수일 때
            arr = arr[:q+1]
    return arr
