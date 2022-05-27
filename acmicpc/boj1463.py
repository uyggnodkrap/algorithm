"""
1로 만들기
https://www.acmicpc.net/problem/1463
"""

import sys
x = int(sys.stdin.readline().rstrip())
dp = [0] * 1000001

for i in range(2, x+1):
    dp[i] = dp[i-1]+1
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[x])