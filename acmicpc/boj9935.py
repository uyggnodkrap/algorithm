"""
문자열 폭발
https://www.acmicpc.net/problem/9935
"""

import sys
input = sys.stdin.readline

string = input().rstrip()
bomb = list(input().rstrip())

len_bomb = len(bomb)
stack = []

for s in string:
    stack.append(s)
    if  s == bomb[-1] and stack[-len_bomb:] == bomb:
        del stack[-len_bomb:]
        
print("FRULA" if not stack else ''.join(stack))