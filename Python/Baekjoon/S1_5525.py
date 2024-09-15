import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
st = input()
startI = st.find('I')

if startI == -1:
    print(0)
    exit()

IOIcount = 0
res = 0
i = startI

while i < m:
    if st[i:i+3] == 'IOI':
        IOIcount += 1
        i += 2
    else:
        if IOIcount >= n:
            res += IOIcount - n + 1
        IOIcount = 0
        i += 1
        
print(res)
        








# io = 0
# isI = False
# nextI = False

# for s in st:
#     if not isI and s == 'I':
#         isI = True
#     elif isI and s == 'O':
#         isI = False
#         io += 1

