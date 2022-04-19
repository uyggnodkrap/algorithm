import re

search_target = '''이상한 전화번호 0030589-5-95826
Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

#아래 부분은 본 강의에서 다루지 않습니다.

regex1 = r'\d+[- ]?\d+[- ]?\d+'
result1 = re.findall(regex1, search_target)

regex2 = r'\d{2}[- ]?\d{3}[- ]?\d{4}'   # {n}: n번 나온다
result2 = re.findall(regex2, search_target)

regex3 = r'\d{2,3}[- ]?\d{3,4}[- ]?\d{4}'   # {n, m}: n~m번 나온다
result3 = re.findall(regex3, search_target)

print(result3)