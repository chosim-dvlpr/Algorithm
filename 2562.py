import sys

my_list = [int(sys.stdin.readline().strip()) for _ in range(9)]
max_num = max(my_list)
print(max_num)
print(my_list.index(max_num)+1)
