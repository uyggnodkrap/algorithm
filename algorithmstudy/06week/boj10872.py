"""
팩토리얼
https://www.acmicpc.net/problem/10872
"""

import sys

n = int(sys.stdin.readline().rstrip())
dp = [1, 1]
for i in range(2, n+1):
    dp.append(dp[-1]*i)
print(dp[-1])