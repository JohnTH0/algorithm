"""
짝지어 제거하기
https://school.programmers.co.kr/learn/courses/30/lessons/12973
lv 2
문자열의 길이 : 1,000,000이하의 자연수
"""

def solution(s:str):
    list_s = []
    for i in range(len(s)):
        list_s.append(s[i])
        if len(list_s) >= 2:
            second_str = list_s[-2]
            first_str = list_s[-1]
            if first_str == second_str:
                del list_s[-2:]
    if len(list_s) == 0:
        return 1
    else:
        return 0 
s = "caabccbc"
print(solution(s))