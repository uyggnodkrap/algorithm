"""
최대공약수와 최소공배수
https://www.acmicpc.net/problem/2609
"""
from math import gcd
a, b = map(int, input().split(' '))
print(f'{gcd(a,b)}\n{(a*b)//gcd(a,b)}')