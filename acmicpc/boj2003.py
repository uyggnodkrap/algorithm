"""
수들의 합 2
https://www.acmicpc.net/problem/2003
"""

import sys


n, m = map(int, sys.stdin.readline().rstrip().split(' '))
a = list(map(int, sys.stdin.readline().rstrip().split(' ')))
l, r, answer = 0, 1, 0

while l <= r and r <= n:
    
    total = sum(a[l:r])

    if total == m:
        answer += 1
        r += 1

    elif total < m:
        r += 1

    else:
        l += 1
        
print(answer)
