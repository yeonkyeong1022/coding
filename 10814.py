from heapq import heappush ,heappop
from sys import stdin 

N = int(stdin.readline())
myList = []

for i in range(N):
    input = stdin.readline().split()
    myList.append([int(input[0]), input[1]])

myList.sort(key = lambda x:x[0])

for i in range(N):
    print(myList[i][0], myList[i][1])