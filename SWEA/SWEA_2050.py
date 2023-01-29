alpha_list = list(map(str, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
new_dict = {}
for idx in range(len(alpha_list)):
    new_dict[alpha_list[idx]] = idx+1

words = list(input())
for word in words:
    print(new_dict[word], end=' ')
