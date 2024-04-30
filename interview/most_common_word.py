"""
가장 흔한 단어
대소문자 구두점 무시
banned 문자열을 제외한 가장 많이 나오는 단어를 출력
lv 1.5
"""
import re
from collections import Counter
def solution(paragraph, banned):
    paragraph = "".join([char for char in paragraph if char.isalpha() or char.isspace()])
    paragraph_list = [val.lower() for val in paragraph.split() if val.lower() not in banned]
    
    # 단일인 경우
    answer = Counter(paragraph_list).most_common(1)[0][0]

    # 복수인 경우
    multi_answer = dict(Counter(paragraph_list))
    max_value = max(multi_answer.values())
    answer_list = [key for key, value in multi_answer.items() if value == max_value]


    return answer

paragraph =  "Bob hit a ball, the hit BALL flew far after it was hit"
banned = ["hit"]
print(solution(paragraph, banned))

"""
정규식 사용방법
\w = 단어문자
^ = Not
word = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
print(word)
"""