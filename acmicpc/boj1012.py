"""
유기농 배추
https://www.acmicpc.net/problem/1012
"""

import sys
from collections import deque


def bfs(i, j):
    queue = deque()
    queue.append((i, j)) # 세로, 가로
    cnt = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft() # 세로, 가로

        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            
            if 0 <= nx <= n-1 and 0 <= ny <= m-1 :               
                if graph[nx][ny] == 1:                    
                    graph[nx][ny] = 0
                    queue.append((nx, ny))
                    cnt += 1

    return cnt


answer = []
for _ in range(int(sys.stdin.readline().rstrip())):
    tmp = []
    m, n, k = map(int, sys.stdin.readline().rstrip().split(' '))

    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        i, j = map(int, sys.stdin.readline().rstrip().split(' '))
        graph[j][i] = 1

    for i in range(n): 
        for j in range(m): 
            if graph[i][j] == 1:
                graph[i][j] = 0
                tmp.append(bfs(i, j))


    answer.append(tmp)


for a in answer:
    print(len(a))
