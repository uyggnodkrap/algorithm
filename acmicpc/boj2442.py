"""
별 찍기 - 5
https://www.acmicpc.net/problem/2442
"""
a = int(input())
for i in range(a):
    print(" "*(a-i) + "*"*(2*i + 1))