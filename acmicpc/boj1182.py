"""
부분수열의 합
https://www.acmicpc.net/problem/1182
"""

from itertools import combinations
import sys
n, s = map(int, sys.stdin.readline().rstrip().split(' '))
arr = list(map(int, sys.stdin.readline().rstrip().split(' ')))

cnt = 0
for i in range(1, n+1):
    comb_arr = combinations(arr, i)

    for c in  comb_arr:
        if sum(c) == s:
            cnt += 1

print(cnt)
