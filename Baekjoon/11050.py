N, K = map(int, input().split())

def pec(a):
    if a == 1 or a == 0:
        return 1
    return pec(a-1)*a

print(int((pec(N)/pec(K))/pec(N-K)))