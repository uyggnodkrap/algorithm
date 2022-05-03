import sys
from collections import deque

def bfs(graph, n, m):
    queue = deque(())
    queue.append((0, 0))

    dx = [1, 0]
    dy = [0, 1]
    cnt = 1
    while queue:
        x, y = queue.popleft()
        
        graph[x][y] = 0
        cnt += 1
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<= nx <= n and 0 <= ny <= m:
                if graph[nx][ny] != 0:
                    graph[nx][ny] = cnt
                    queue.append((nx, ny))
                    if nx == n and ny == m:
                        return cnt
 
graph = []
N, M = map(int, sys.stdin.readline().rstrip().split(' '))
for _ in range(N):
    graph.append(list(map(int, list(sys.stdin.readline().rstrip()))))


# print(bfs(graph, N-1, M-1))
