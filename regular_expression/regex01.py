import re

# 주소록입니다. 이후 강의에서 모두 이 search_target을 사용합니다.
search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''



# 정규표현식과 일치하는 부분을 모두 찾아주는 파이썬 코드입니다.
regex1 = r'\d'              # \d: digit -> 숫자 하나
result1 = re.findall(regex1, search_target)

regex2 = r'\w'              # \w: word -> 숫자와 문자 하나
result2 = re.findall(regex2, search_target)

regex3 = r'\d+'             # \d+ digit+ -> 숫자 하나 또는 그 이상
result3 = re.findall(regex3, search_target)

regex4 = r'[1-9]\d+'        # [1-9]\d+ -> 앞자리가 0이 아닌 두자리 이상의 숫자
result4 = re.findall(regex4, search_target)

regex5 = r'[1-9]\d*'        # [1-9]\d+ -> 앞자리가 0이 아닌 숫자 하나 또는 그 이상
result5 = re.findall(regex5, search_target)

regex6 = r'\d+-?\d+-?\d+'   # '\d+-?\d+-?\d+ -> ?는 있거나 없거나로, 전화번호 표현식이다
result6 = re.findall(regex6, search_target)

regex7 = r'\d+[- ]?\d+[- ]?\d+'   # '\d+-?\d+-?\d+ -> ?는 있거나 없거나로, 전화번호 표현식이다
result7 = re.findall(regex7, search_target)

print(" ".join(result6))
print(" ".join(result7))
