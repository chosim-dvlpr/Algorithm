import sys

input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n+1)]

preOrder_result = []
inOrder_result = []
postOrder_result = []

for _ in range(n):
    root, left, right = input().split()
    if left == '.':
        left = None
    else:
        left = ord(left) - 64
    if right == '.':
        right = None
    else:
        right = ord(right) - 64
    arr[ord(root) - 64] = [left, right]

def preOrder(node):
    preOrder_result.append(node)

    if arr[node][0] != None:
        preOrder(arr[node][0])
    if arr[node][1] != None:
        preOrder(arr[node][1])

def inOrder(node):
    if arr[node][0] != None:
        inOrder(arr[node][0])
    
    inOrder_result.append(node)

    if arr[node][1] != None:
        inOrder(arr[node][1])

def postOrder(node):
    if arr[node][0] != None:
        postOrder(arr[node][0])
    
    if arr[node][1] != None:
        postOrder(arr[node][1])
    
    postOrder_result.append(node)


preOrder(1)
inOrder(1)
postOrder(1)

for num in preOrder_result:
    print(chr(num+64), end="")
print()
for num in inOrder_result:
    print(chr(num+64), end="")
print()
for num in postOrder_result:
    print(chr(num+64), end="")