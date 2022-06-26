"""
수 고르기
https://www.acmicpc.net/problem/2230
"""

import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().rstrip().split(' '))
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort(reverse = True)
print(arr)
# l, r, answer = 0, n-1, sys.maxsize

# while l <= r and r <= n:
#     if arr[r] - arr[l] >= m:
#         answer = min(answer, r - l)
