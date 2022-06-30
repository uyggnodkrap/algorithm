"""
달팽이는 올라가고 싶다. 
https://www.acmicpc.net/problem/2869
"""
import sys
import math

a, b, v = map(int, sys.stdin.readline().rstrip().split(' '))
print(math.ceil((v -b) / (a - b)))