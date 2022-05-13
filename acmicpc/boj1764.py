"""
듣보잡
https://www.acmicpc.net/problem/1764
"""

import sys

n, m = map(int, sys.stdin.readline().rstrip().split(' '))
p = []
for _ in range(n+m):
    p.append(sys.stdin.readline().rstrip())
p.sort()

answer = []
for i in range(n+m-1):
    if p[i] == p[i+1]:
        answer.append(p[i+1])

print(len(answer))
for a in answer:
    print(a)
