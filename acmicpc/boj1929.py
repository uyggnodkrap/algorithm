"""
소수 구하기
https://www.acmicpc.net/problem/1929
"""
import sys


def isPrime(x):
    prime = [False, False] + [True] * (x - 1)

    for i in range(2, x + 1):
        if prime[i]:
            for j in range(i + i, x + 1, i):
                prime[j] = False

    return [i for i in range(len(prime)) if prime[i]]


M, N = map(int, sys.stdin.readline().split(' '))

answer = [a for a in isPrime(N) if M <= a <= N]
for a in answer:
    print(a)
