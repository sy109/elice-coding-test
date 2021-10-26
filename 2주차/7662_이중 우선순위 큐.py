import sys
import heapq as hq

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
ans = []
maxheap = []
minheap = []

for iter in range(N):
    T = int(input())
    for i in range(T):
        command, number = input().split()
        if command == "I":
            hq.heappush(minheap,int(number))
            hq.heappush(maxheap,-int(number))
        else:
            if len(minheap) == 0 or len(maxheap)==0:
                continue
            else:
                if number == "1":
                    minheap.remove(max(minheap))
                    hq.heappop(maxheap)
                else:
                    maxheap.remove(max(maxheap))
                    hq.heappop(minheap)
        # print("maxheap",maxheap)
        # print("minheap",minheap)
    if len(maxheap) == 0 or len(minheap)==0:
        ans.append(1)
    else:
        ans.append((-maxheap[0], minheap[0]))
    maxheap.clear()
    minheap.clear()

for i in ans:
    if i == 1: print("EMPTY")
    else: print(*i)