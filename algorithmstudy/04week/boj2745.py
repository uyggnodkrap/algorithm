"""
진법 변환
https://www.acmicpc.net/problem/2745
"""
import sys

n, b = sys.stdin.readline().rstrip().split(' ')

alphabet = {chr(ord('A')+i): 10+i for i in range(26)} 

n = list(n)[::-1]
b = int(b)

answer = 0
for i in range(len(n)):
    if n[i] in alphabet:
        tmp = alphabet[n[i]]
    else:
        tmp = int(n[i])
    answer += tmp*(b**i)

print(answer)
    