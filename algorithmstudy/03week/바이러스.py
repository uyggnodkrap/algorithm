"""
바이러스
https://www.acmicpc.net/problem/2606
"""


import sys
from collections import deque
def bfs(computer):
    queue, visit = deque([]), []
    queue.append(1)

    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            queue.extend(computer[node])
    
    return visit


computer = {i+1: [] for i in range(int(sys.stdin.readline().rstrip()))}
for _ in range(int(sys.stdin.readline().rstrip())):
    a, b = map(int,sys.stdin.readline().rstrip().split(' '))
    computer[a].append(b)
    computer[b].append(a)

print(len(bfs(computer))-1)


