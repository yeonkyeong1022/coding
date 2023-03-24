from sys import stdin 

N = int(stdin.readline())
L = list(map(int, stdin.readline().split()))
result = []
for i in range(N-1, -1, -1):
    result.insert(L[i], i+1)

for i in result:
    print(i, end=' ')