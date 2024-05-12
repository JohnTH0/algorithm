"""
숫자 짝꿍
https://school.programmers.co.kr/learn/courses/30/lessons/131128
lv 1
"""
from collections import Counter
def solution(X:str, Y:str) -> str:
    dict_x = dict(Counter(list(X)))
    dict_y = dict(Counter(list(Y)))
    intersection_number_list = []
    for key in dict_x.keys() & dict_y.keys():
        min_val = min(int(dict_x[key]), int(dict_y[key]))
        intersection_number_list.extend([key]*min_val)

    if not intersection_number_list:
        return "-1"
    
    if len(intersection_number_list) == intersection_number_list.count("0"):
        return "0"
    
    result = "".join(sorted(intersection_number_list, key=lambda x: x, reverse=True))

    return result
X = "5525"
Y = "1255"

solution(X, Y)