Test_num = int(input())

for _ in range(Test_num):
    OX_str = input()
    sums = 0
    adds = 0
    for i in range(len(OX_str)):
        if OX_str[i] == 'O':
            adds += 1
            sums += adds
        elif OX_str[i] == 'X':
            adds = 0
    print(sums)
