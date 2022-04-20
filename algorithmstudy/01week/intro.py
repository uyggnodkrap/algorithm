"""
stack
LIFO 구조를 갖는 자료구조로
데이터의 접근이 한 쪽에서만 가능함

ex) 웹페이지 이전 페이지, 다음페이지
    DFS
    함수의 호출
"""
# stack 직접 구현
class Stack(list):
    push = list.append

    def peek(self):
        return self[-1]

    # pop: 리스트에 pop 기능이 있음

s1 = Stack()
s1.push(1)
s1.push(5)
s1.push(10)
print("===== stack 직접 구현 =====")
print(f'stack:  {s1}')
print(f'peeked value: {s1.peek()}\n')
print(f'stack:  {s1}')
print(f'popped value: {s1.pop()}\n')
print(f'stack:  {s1}')
print(f'popped value: {s1.pop()}\n')
print(f'stack:  {s1}')
print(f'peeked value: {s1.peek()}\n')
print(f'stack:  {s1}')
print(f'popped value: {s1.pop()}\n')
print(f'stack:  {s1}')

# 2. list 활용
s2 = []
s2.append(1)
s2.append(5)
s2.append(10)
print("\n\n===== stack list 활용 =====")
print(f'stack:  {s2}')
print(f'peeked value: {s2[-1]}\n')
print(f'stack:  {s2}')
print(f'popped value: {s2.pop()}\n')
print(f'stack:  {s2}')
print(f'popped value: {s2.pop()}\n')
print(f'stack:  {s2}')
print(f'peeked value: {s2[-1]}\n')
print(f'stack:  {s2}')
print(f'popped value: {s2.pop()}\n')
print(f'stack:  {s2}')
