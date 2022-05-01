"""
사탕게임
https://www.acmicpc.net/problem/3085
"""

import sys
N = int(sys.stdin.readline().rstrip())
candy = []
for _ in range(N):
    candy.append(list(sys.stdin.readline().rstrip()))


for i in range(N):
    for j in range(N-1):
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        # 가로



        # 세로
        candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
