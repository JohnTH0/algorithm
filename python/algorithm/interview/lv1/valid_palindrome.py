"""
회문 검증 문제
대소문자 구분하지 않음
영문 숫자만 대상
lv 1
"""

def solution(sentence):
    origin_sentence = [text.lower() for text in sentence if text.isalnum() == True]
    reverse_sentence = origin_sentence[::-1]
    return True if origin_sentence == reverse_sentence else False

sentence = "A man, a plan, a canal: Panama"
solution(sentence)

"""
파이썬 문자열 슬라이싱 속도
리스트 슬라이싱: 0.499
reverse: 2.46
reversed() + join(): 2.49
for loop: 5.5
while loop: 9.4
재귀 24.3
"""