"""
올바른 괄호
https://school.programmers.co.kr/learn/courses/30/lessons/12909
lv 2
"""

def solution(s):    
    list_s = []
    for i in s:
        list_s.append(i)

        if list_s[-2:] == ['(',')']:
            del list_s[-2:]
    return True if not list_s else False
    
s = "(())()"
print(solution(s))