"""
햄버거 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/133502
lv 1
"""

def solution(ingredient):
    target_list = [1, 2, 3, 1]
    count = 0
    current_stack = []

    for i in ingredient:
        current_stack.append(i)

        if current_stack[-4:] == target_list:
            del current_stack[-4:]
            count +=1

    return count
