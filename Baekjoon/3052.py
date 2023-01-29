import sys

num_list = [int(sys.stdin.readline().strip())%42 for _ in range(10)]
new_list = list(set(num_list))
print(len(new_list))
