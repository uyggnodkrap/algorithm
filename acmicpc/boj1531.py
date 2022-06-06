"""
투명
https://www.acmicpc.net/problem/1531
"""
import sys

n, m = map(int, sys.stdin.readline().rstrip().split(' '))
grid = [ [0] * 100 for _ in range(100)]
cnt = 0

for _ in range(n):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split(' '))
    
    for i in range(x1-1, x2):
        for j in range(y1-1, y2):
            grid[i][j] += 1

for i in range(100):
    for j in range(100):
        if grid[i][j] > m:
            cnt += 1

print(cnt)
