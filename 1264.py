# Baekjoon 1264

while 1:
    my_string = input()

    if my_string == '#':
        break
    sums = 0

    for aei in my_string:
        if aei in 'aeiouAEIOU':
            sums += 1
    print(sums)
