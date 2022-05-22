"""
해싱
https://www.acmicpc.net/problem/15829
"""

import sys
l = int(sys.stdin.readline())
s = sys.stdin.readline()
m = 1234567891
r = 31
answer = 0
for i in range(l):
    answer += (ord(s[i]) - 96) * (r**i)

print(answer%m)