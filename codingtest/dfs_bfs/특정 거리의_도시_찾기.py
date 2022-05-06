"""
특정 거리의 도시 찾기
https://www.acmicpc.net/problem/18352
"""


import sys
from collections import deque

def bfs1(graph, x, k):
    queue = deque()
    visited, answer = [], []
    cnt = 0
    queue.append((x, 0))
    visited.append(x)
    while queue:
        node, cnt = queue.popleft()

        if cnt == k:
            answer.append(node)
        elif cnt < k:
            for n in graph[node]:
                if n not in visited:
                    visited.append(n)
                    queue.append((n, cnt+1))

    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for a in answer:
            print(a)

        

def bfs2 (graph, x, k, n):
    answer = [-1] * (n+1)
    answer[x] = 0 
    queue = deque([x])
    while queue:
        node = queue.popleft()

        for next_node in graph[node]:
            if answer[next_node] == -1:
                answer[next_node] = answer[node] + 1
                queue.append(next_node)
    
    if k not in answer:
        print(-1)
    else:
        for i in range(n+1):
            if answer[i] == k:
                print(i)



n, m, k, x  = map(int, sys.stdin.readline().rstrip().split(' '))
graph = {i+1: [] for i in range(n)}

for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split(' '))
    graph[i].append(j)

bfs1(graph, x, k)

bfs2(graph, x, k, n)

