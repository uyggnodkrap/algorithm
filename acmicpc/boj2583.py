"""
영역 구하기
https://www.acmicpc.net/problem/2583
"""
import sys

m, n, k = map(int, sys.stdin.readline().rstrip().split(' '))
# m: 세로
# n: 가로

graph = [[0] * (n+1) for _ in range(m+1)]

# for _ in range(k):
#     q, w, e, r = map(int, sys.stdin.readline().rstrip().split(' '))

for g in graph:
    print(g)
