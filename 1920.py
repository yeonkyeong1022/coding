from heapq import heappush ,heappop
import bisect
from sys import stdin 

N = int(stdin.readline())
List = list(map(int, stdin.readline().split()))
# heapList=[]
# for i in List:
#     heappush(heapList, i)

List.sort()

M = int(stdin.readline())
findList = list(map(int, stdin.readline().split()))


for i in range(len(findList)):
    findIdx = bisect.bisect(List, findList[i])-1
    if List[findIdx]==findList[i]:
        print(1)
    else:
        print(0)
