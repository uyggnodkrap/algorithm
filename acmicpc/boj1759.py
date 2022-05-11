"""
암호 만들기
https://www.acmicpc.net/problem/1759
"""
import sys
from itertools import combinations


l, c = map(int, sys.stdin.readline().rstrip().split(' '))
arr = list(sys.stdin.readline().rstrip().split(' '))
arr.sort()
code = combinations(arr, l)

for a in code:
    t = 0
    for i in a:
        if i in "aeiou":
            t += 1

    if t != 0 and l - t >= 2:
        print(''.join(a))
        