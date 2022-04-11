"""
소수
https://www.acmicpc.net/problem/2581
"""

a = int(input())
b = int(input())

def isPrime(x):

    arr = [False, False] + [True] * (x-1)
    prime = []
    for i in range(2, x+1):
        if arr[i]:
            prime.append(i)
            for j in range(i*2,  x+1, i):
                arr[j] = False

    return prime

answer = [k for k in isPrime(max(a, b)) if a<= k <= b]
print(f'{sum(answer)}\n{answer[0]}') if answer else print(-1)