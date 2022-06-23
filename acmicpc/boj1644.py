"""
소수의 연속합
https://www.acmicpc.net/problem/1644
"""

import sys


n = int(sys.stdin.readline().rstrip())
answer = 0
l, r = 0, 1
prime_index = []
prime = [False, False] + [True] * (n - 1)
for i in range(2, n+1):
    if prime[i]:
        for j in range(i+i, n+1, i):
            prime[j] = False

prime_index = [i for i in range(len(prime)) if prime[i]]


while l <= r and r <= n:
    total = sum(prime_index[l:r])

    if total == n:
        answer += 1
        l += 1
    elif total < n:
        r += 1
    else: 
        l += 1
        
print(answer)
