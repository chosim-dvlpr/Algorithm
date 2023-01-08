a = [1,2,3]
b = [1,3,5,7,9]

min_list = min(len(a),len(b))
sub_list = abs(len(a)-len(b))
new_list = []
my_sum = 0

def length(a, b):
    for j in range(sub_list+1):
        if len(a) > len(b):
            b = [0] + b
        elif len(a) < len(b):
            a = [0] + a
        else:
            print(a, b)

for i in range(min_list):
    my_sum += a[i]*b[i]
new_list.append(my_sum)
print('new_list :',new_list)



