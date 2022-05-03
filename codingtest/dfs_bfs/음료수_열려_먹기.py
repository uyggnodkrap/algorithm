import sys
from collections import deque

def dfs (grid, i, j):
    stack = deque(())
    stack.append((i, j))
    cnt = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while stack:
        
        x, y = stack.pop()
        grid[x][y] = "1"
        
        for t in range(4):
            nx = dx[t] + x
            ny = dy[t] + y

            if 0<=nx<N and 0<= ny < M:
                if grid[nx][ny] == "0":
                    cnt += 1
                    grid[nx][ny] = "1"
                    stack.append((nx, ny))
                    
    return cnt


N, M = map(int, sys.stdin.readline().rstrip().split(' '))
grid = []
for _ in range(N):
    grid.append(list(sys.stdin.readline().rstrip()))
answer = []


for i in range(N):
    for j in range(M):
        if grid[i][j] == "0":
            answer.append(dfs(grid, i, j))

print(len(answer))
