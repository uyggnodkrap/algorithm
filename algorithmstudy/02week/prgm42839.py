<<<<<<< HEAD
"""
소수 찾기
https://programmers.co.kr/learn/courses/30/lessons/42839
"""

from itertools import permutations


def isPrime(x):
    prime = [False, False] + [True] * (x - 1)

    for i in range(2, x + 1):
        if prime[i]:
            for j in range(i + i, x + 1, i):
                prime[j] = False

    return [i for i in range(len(prime)) if prime[i]]


def solution(numbers):
    numbers = list(numbers)
    answer = set()

    for i in range(1, len(numbers) + 1):
        arr = set(permutations(numbers, i))
        for a in arr:
            answer.add(int("".join(a)))

    prime = isPrime(max(answer))

    return len([a for a in answer if a in prime])
=======
"""
소수 찾기
https://programmers.co.kr/learn/courses/30/lessons/42839
"""

from itertools import permutations


def isPrime(x):
    prime = [False, False] + [True] * (x - 1)

    for i in range(2, x + 1):
        if prime[i]:
            for j in range(i + i, x + 1, i):
                prime[j] = False

    return [i for i in range(len(prime)) if prime[i]]


def solution(numbers):
    numbers = list(numbers)
    answer = set()

    for i in range(1, len(numbers) + 1):
        arr = set(permutations(numbers, i))
        for a in arr:
            answer.add(int("".join(a)))

    prime = isPrime(max(answer))

    return len([a for a in answer if a in prime])
>>>>>>> a81508b (완전탐색/이분탐색)
