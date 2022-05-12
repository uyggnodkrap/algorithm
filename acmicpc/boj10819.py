"""
차이를 최대로
https://www.acmicpc.net/problem/10819
"""

import sys
from itertools import permutations

n = int(sys.stdin.readline().rstrip())
arr1 = list(map(int, sys.stdin.readline().rstrip().split(' ')))

case = permutations(arr1)
answer = []
for c in case:
    a = 0
    for i in range(n-1):
        a += abs(c[i] - c[i+1])
    answer.append(a)
print(max(answer))




