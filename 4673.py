s_list = list(range(1,100))

for num in range(1,10):
    num_str = str(num)
    sums = 0
    for i in range(len(num_str)):
        sums += int(num_str[i])
    s = num + sums
    if s in s_list:
        s_list.pop(s)
    print(s_list)
