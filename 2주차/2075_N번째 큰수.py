import sys
import heapq as hq

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
ans = [[] for i in range(N)]

for i in range(N):
    lis = list(map(int,input().split()))
    for count in range(len(lis)):
        hq.heappush(ans[count],-lis[count%N])



    