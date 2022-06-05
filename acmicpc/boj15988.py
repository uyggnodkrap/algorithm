"""
1, 2, 3 더하기 3
https://www.acmicpc.net/problem/15988
"""

import sys 
dp = [0, 1, 2, 4]
for i in range(4, 1000001):
    dp.append((dp[-3] + dp[-2] + dp[-1])%1000000009)
for _ in range(int(sys.stdin.readline().rstrip())):
    print(dp[int(sys.stdin.readline().rstrip())])

