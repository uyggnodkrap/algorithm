"""
DFS와 BFS
https://www.acmicpc.net/problem/1260
"""
import sys
from collections import deque

def dfs(graph, v):
    stack = deque([])
    visited = []

    stack.append(v)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node in graph:
                x = list(set(graph[node]) - set(visited))
                x.sort(reverse = True)
                stack.extend(x)
    
    return ' '.join(map(str, visited))

def bfs(graph, v):
    queue = deque([])
    visited = []
    queue.append(v)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            if node in graph:
                x = list(set(graph[node]) - set(visited))
                x.sort()
                queue.extend(x)

    return ' '.join(map(str, visited))

n, m, v = map(int, sys.stdin.readline().rstrip().split(' '))
graph = {i+1: [] for i in range(n)}

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    graph[a].append(b)
    graph[b].append(a)

print(dfs(graph, v))
print(bfs(graph, v))
