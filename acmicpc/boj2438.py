"""
별 찍기 - 1
https://www.acmicpc.net/problem/2438
"""

for i in range(int(input())):
    for j in range(i+1):
        print("*", end='')
    print()