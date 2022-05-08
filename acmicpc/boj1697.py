"""
숨바꼭질
https://www.acmicpc.net/problem/1697
"""

import sys
from collections import deque
n, k = map(int, sys.stdin.readline().rstrip().split(' '))


def bfs(n, k):
    LIMIT = 100000
    visit = [0 for _ in range(LIMIT+1)]

    queue = deque()
    queue.append(n)

    while queue:
        node = queue.popleft()
        if node == k:
            print(visit[node])
            break
            
        for i in (node -1, node + 1, node*2):
            if 0 <= i <= LIMIT and visit[i] == 0:
                visit[i] = visit[node] + 1
                queue.append(i)


bfs(n, k)