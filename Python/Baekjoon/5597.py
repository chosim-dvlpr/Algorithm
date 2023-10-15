submit = [int(input().strip()) for _ in range(28)]
new_list = []

for i in range(1,31):
    if i not in submit:
        new_list.append(i)
print(min(new_list))
print(max(new_list))
