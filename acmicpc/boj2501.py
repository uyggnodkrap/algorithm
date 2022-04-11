"""
약수 구하기
https://www.acmicpc.net/problem/2501
"""

a, b = map(int, input().split(' '))
arr = []
for i in range(1, a+1):
    if a % i == 0:
        arr.append(i)
if b <= len(arr):
    print(arr[b-1])
else:
    print(0)