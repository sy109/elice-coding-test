
"""
    문제 이름: 완전 이진 트리
    문제 번호: 9934
    문제 링크: https://www.acmicpc.net/problem/9934
    난이도: Silver I
    태그: 구현, 재귀, 트리
"""
import sys 

def input(): return sys.stdin.readline().rstrip()


def solve(k, nodes):
    result = [[] for _ in range(k)]
    def recu(start, end, depth):
        if start == end:
            result[depth].append(nodes[start])
            return
        mid = (start+end)//2
        result[depth].append(nodes[mid])

        recu(start, mid-1, depth+1)
        recu(mid+1, end, depth+1)
    recu(0, len(nodes)-1 , 0)
    return result


k = int(input())
nodes = [int(x) for x in input().split()]

result = solve(k, nodes)

for lst in result:
    print(*lst)
