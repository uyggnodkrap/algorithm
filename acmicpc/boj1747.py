"""
소수&팰린드롬
https://www.acmicpc.net/problem/1747
"""
import sys
n = int(sys.stdin.readline())


def isPrime(n):
    p = 1000000
    arr = [False, False] + [True] * (p-1)

    for i in range(2, p+1):
        if arr[i]:
            for j in range(i*2, p+1, i):
                arr[j] = False

    return [i for i in range(n, len(arr)) if arr[i]]


def palindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False
result = 0
for a in isPrime(n):
    if palindrome(a):
        result = a
        break

if result != 0:
    print(result)
else:
    print(1003001)
