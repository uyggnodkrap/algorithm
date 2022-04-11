"""
쉽게 푸는 문제
https://www.acmicpc.net/problem/1292
"""

x, y = map(int, input().split(' '))

i = 0
arr = []
while len(arr) <= y:
    i += 1
    for j in range(0, i):
        arr.append(i)

print(sum([arr[a] for a in range(x-1, y)]))