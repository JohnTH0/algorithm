"""
No.819
https://leetcode.com/problems/most-common-word/description/
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned.
It is guaranteed there is at least one word that is not banned, and that the answer is unique.
The words in paragraph are case-insensitive and the answer should be returned in lowercase.
lv 1.5
"""

import re
from collections import Counter
def solution(paragraph, banned):
    """
    정규식 사용
    \w = 
    ^ = Not
    => 문자가 아닌 값들을 공백으로 변환
    """
    paragraph_list = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    return Counter(paragraph_list).most_common(1)[0][0]

# def solution(paragraph, banned):
#     # 특수문자를 변환하기 위한 빈 문자열 선언
#     convert_paragraph = ""
#     for i in range(len(paragraph)):
#         """
#         반복문을 순회하면서 문자인 경우 소문자로 변환하여 추가,
#         공백인 경우 그대로 공백으로 추가,
#         그외 특수문자인 경우, 앞뒤 값을 비교하여 추가
#         """
#         if paragraph[i].isalpha():
#             convert_paragraph += paragraph[i].lower()
#         elif paragraph[i].isspace():
#             convert_paragraph += " "
#         else:
#             if i + 1 < len(paragraph):
#                 if paragraph[i-1].isalpha() and paragraph[i+1].isalpha():
#                     convert_paragraph += " "
#                 elif paragraph[i-1].isspace() or paragraph[i+1].isspace():
#                     continue
#             else:
#                 if paragraph[i-1].isalpha():
#                     convert_paragraph += " "
#                 elif paragraph[i-1].isspace():
#                     continue
                
#     # 변환한 문자열을 공백으로 나눈 후, banned에 포함되지 않는 단어 리스트 출력
#     answer_list = [word for word in convert_paragraph.split() if word not in banned]

#     return Counter(answer_list).most_common(1)[0][0]

paragraph =  "Bob hit a ball, the hit BALL flew far after it was hit"
banned = ["hit"]

solution(paragraph, banned)