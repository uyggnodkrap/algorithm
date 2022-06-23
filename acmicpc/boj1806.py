"""
부분합
https://www.acmicpc.net/problem/1806
"""
import sys


n, s = map(int, sys.stdin.readline().rstrip().split(' '))
a = list(map(int, sys.stdin.readline().rstrip().split(' ')))
l, r = 0, 1
answer = sys.maxsize
sum_a = [0] * (n+1)

for i in range(1, n+1):
    sum_a[i] = sum_a[i-1] + a[i-1]

while l <= r and r <= n:
    if sum_a[r]- sum_a[l] >= s:
        answer = min(answer, r - l)
        l += 1
    else:
        r += 1

print(answer if answer != sys.maxsize else 0)
    
