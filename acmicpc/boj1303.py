"""
전쟁 - 전투
https://www.acmicpc.net/problem/1303
"""

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, team):
        queue = deque(())
        queue.append((x, y))

        graph[x][y] = "0"
        cnt = 1

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if graph[nx][ny] != 0 and graph[nx][ny] == team:
                    queue.append((nx, ny))
                    graph[nx][ny] = 0
                    cnt += 1

        return cnt**2

m, n = map(int, input().split(' '))
graph = [list(input().strip()) for _ in range(n)]

w, b = 0, 0

for i in range(n):
    for j in range(m):
        if graph[i][j] != "0":
            if graph[i][j] == "W":
                w += bfs(i, j, "W")

            elif graph[i][j] == "B":
                b += bfs(i, j, "B")

print(w, b)