"""
ATM
https://www.acmicpc.net/problem/11399
"""

import sys
n = int(sys.stdin.readline().rstrip())
p = list(map(int,  sys.stdin.readline().rstrip().split(' ')))
p.sort()
print(sum([p[i] * (n-i) for i in range(n)]))