from sys import stdin 
from heapq import heappush, heappop 

heap = set([])

N = int(stdin.readline())
for i in range(N):
    heap.add(stdin.readline().rstrip())
heap = list(heap)

heap.sort()
heap.sort(key=lambda x:len(x))
for i in heap:
    print(i)