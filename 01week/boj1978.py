"""
소수 찾기
https://www.acmicpc.net/problem/1978
"""

def isPrime(x):
    prime = [False, False] + [True] * (x-1)
    for i in range(2, x+1):
        if prime[i]:
            for j in range(i*2, x+1, i):
                prime[j] = False
    return prime

q = int(input())
arr = list(map(int, input().split(' ')))

cnt = 0
ans = isPrime(max(arr))
for i in arr:
    if ans[i]:
        cnt += 1

print(len([x for x in arr if ans[x]]))