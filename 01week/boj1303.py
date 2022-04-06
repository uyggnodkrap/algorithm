"""
전쟁 - 전투
https://www.acmicpc.net/problem/1303
"""

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs_w(graph, x, y):

        queue = deque(())
        queue.append((x, y))

        graph[x][y] = 0
        cnt = 1
        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= s or ny < 0 or ny >= t:
                    continue
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx, ny))
                    cnt += 1

        return cnt

s, t = map(int, input().split(' '))
graph = []

for _ in range(s):
    graph.append(list(input()))

for g in graph:
    print(g)

# 1. W
w, b = [], []
for i in range(s):
    for j in range(t):
        if graph[i][j] == "W":
            w.append(dfs_w(graph, i, j))
print(w)
# 2. B


