"""
jadencase 문자열 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/12951
lv 2
"""

def solution(s):
    return " ".join(word.capitalize() for word in s.split(' '))

s = "3people unFollowed me"
solution(s)