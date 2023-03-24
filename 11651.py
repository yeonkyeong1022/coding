from sys import stdin 

N = int(stdin.readline())
point = []
for i in range(N):
    point.append(list(map(int, stdin.readline().split())))
point.sort()
point.sort(key = lambda x:x[1])

for i in range(N):
    print(point[i][0], point[i][1])

