"""
숫자 카드 2
https://www.acmicpc.net/problem/10816
"""

import sys
_ = int(sys.stdin.readline())
card = list(sys.stdin.readline().rstrip().split(' '))
_ = int(sys.stdin.readline())
arr = list(sys.stdin.readline().rstrip().split(' '))

hash_card = {a: 0 for a in arr}

for c in card:
    if c in hash_card.keys():
        hash_card[c] += 1

print(' '.join(str(hash_card[m]) if m in hash_card else '0' for m in arr))