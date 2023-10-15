num = int(input())
num2 = num

new_num = 0
n = 0

if new_num == num:
    n += 1

while new_num != num:
    if num2 >= 10:
        new_sum = num2//10 + num2%10
        new_num = (num2%10)*10 + new_sum%10
        num2 = new_num
        n += 1
        continue
        
    else:
        new_num = num2*10 + num2
        num2 = new_num
        n += 1
        continue
        
print(n)
