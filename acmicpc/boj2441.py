"""
별 찍기 - 4
https://www.acmicpc.net/problem/2441
"""
a = int(input())
for i in range(a):
    print(" " * (i) + "*" * (a-i))
