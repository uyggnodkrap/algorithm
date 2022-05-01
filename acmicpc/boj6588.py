"""
골드바흐의 추측
https://www.acmicpc.net/problem/6588
"""
import sys


t = 100000
prime = [False, False] + [True] * (t - 1)

for i in range(2, 1001):
    if prime[i]:
        for j in range(i+i, t+1, i):
            prime[j] = False

prime = [i for i in range(len(prime)) if prime[i]][1:]

while True:
    x = int(sys.stdin.readline().rstrip())
    if x == 0: break

    else:
        b = 0
        for a in prime:
            if x - a in prime:
                b = x - a
                print(f'{x} = {a} + {b}')
                break
        if b == 0:
            print("Goldbach's conjecture is wrong.")


