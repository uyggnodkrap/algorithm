
"""
\s:  공백 문자(스페이스, 탭, 뉴라인)
\S:  공백 문자를 제외한 문자
\D:  숫자를 제외한 문자
\W:  글자 대표 문자를 제외한 글자들(특수문자, 공백 등)
"""
import re

search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

# 정규표현식과 일치하는 부분을 모두 찾아주는 파이썬 코드입니다.

regex1 = r'[aeiou]'     # []: 모음 선택 -> 대괄호 안의 글자를 모두 선택하고 싶을 때
result1 = re.findall(regex1, search_target)

regex2 = r'[a-z]'       # [a-z]: 소문자 모두 선택
result2 = re.findall(regex2, search_target)

regex3 = r'[a-z]+'      # [a-z]+: 연속된 소문자 모두 선택
result3 = re.findall(regex3, search_target)

regex4 = r'[가-힣]+'      # [가-힣]+: 연속된 한글 단어 선택
result4 = re.findall(regex4, search_target)

print(" ".join(result4))