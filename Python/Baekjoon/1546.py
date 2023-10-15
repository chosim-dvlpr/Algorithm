import sys

N = int(sys.stdin.readline())
grade_list = list(map(int, sys.stdin.readline().split()))
M = max(grade_list)
new_grade = [i/M*100 for i in grade_list]
new_avg = sum(new_grade)/N
print(new_avg)
