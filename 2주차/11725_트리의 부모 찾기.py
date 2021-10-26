import sys
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
a = defaultdict(int)
for _ in range(1,N):
    node1, node2 = map(int,input().split())
    if node1 == 1:
        a[node2] = 1
    elif node2 == 1:
        a[node1] = 1
    else:
        if a[node1] != 0:
            a[node2] = node1
        else:
            a[node1] = node2
for i in range(2,N+1):
    print(a[i])