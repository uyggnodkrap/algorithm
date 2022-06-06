"""
1, 2, 3 더하기
https://www.acmicpc.net/problem/9095
"""

import sys

dp = [0, 1, 2, 4]

for _ in range(4, 12):
    dp.append(dp[-1] + dp[-2] + dp[-3])

for _ in range(int(sys.stdin.readline().rstrip())):
    print(dp[int(sys.stdin.readline().rstrip())])
    