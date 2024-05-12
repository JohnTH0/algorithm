"""
문자열 내림차순으로 배치하기
https://school.programmers.co.kr/learn/courses/30/lessons/12917
lv 1
"""
def solution(s:str) -> str:
    upper_s = sorted([char for char in list(s) if char.isupper()],reverse=True)
    lower_s = sorted([char for char in list(s) if char.islower()],reverse=True)
    sort_s = lower_s + upper_s
    return "".join(sort_s)
s = "Zbcdefg"
solution(s)