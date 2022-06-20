"""
피보나치 수
https://www.acmicpc.net/problem/2747
"""

import sys
dp = [0, 1, 1]
n = int(sys.stdin.readline().rstrip())
for _ in range(3, n+1):
    dp.append(dp[-1] + dp[-2])
print(dp[-1])