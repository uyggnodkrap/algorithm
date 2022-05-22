"""
럭키 스트레이트
https://www.acmicpc.net/problem/18406
"""

n = input()
len_n = len(n)
a, b = 0, 0
for i in range(len_n//2):
    a += int(n[i])
    b += int(n[len_n-i-1])

print("LUCKY" if a == b else "READY")