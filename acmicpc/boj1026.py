"""
보물
https://www.acmicpc.net/problem/1026
"""

import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split(' ')))
b = list(map(int, sys.stdin.readline().rstrip().split(' ')))

a.sort()
b.sort(reverse = True)
print(a)
print(b)
print(sum([i * j for i, j in zip(a,b)]))


"""
5
1 1 1 6 0
2 7 8 3 1

6 + 2 + 7 + 2 + 3
"""