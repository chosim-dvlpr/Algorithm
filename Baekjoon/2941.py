N = input()

word_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0

for word in word_list:
    cnt += N.count(word)
    N = N.replace(word, ' ')
print(len(N.replace(' ', ''))+cnt)
    
    
