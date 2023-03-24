from sys import stdin 
from bisect import bisect_left, bisect_right
N = int(stdin.readline())
myList = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
target = list(map(int, stdin.readline().split()))

myList.sort()

for i in target:
    print(bisect_right(myList, i)-bisect_left(myList, i), end=' ')
