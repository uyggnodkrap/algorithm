"""
연결 요소의 개수
https://www.acmicpc.net/problem/11724
"""

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split(' '))


def dfs(i):
    visit = []
    stack = deque([i])

    while stack:
        node = stack.popleft()

        if node not in visit and graph[node] != "X":
            visit.append(node)
            stack.extend(graph[node])
            graph[node] = "X"

    return visit


graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split(' '))
    graph[a].append(b)
    graph[b].append(a)

answer = []
for i in range(1, n + 1):
    if graph[i] != "X":
        answer.append(dfs(i))

print(len(answer))
