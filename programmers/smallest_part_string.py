"""
크기가 작은 부분 문자열
https://school.programmers.co.kr/learn/courses/30/lessons/147355
lv 1
"""
def solution(t, p):
    p_len = len(p)
    t_list = []

    for i in range(0,len(t)):
        val = t[i:i+p_len]
        if len(val) < p_len:
            continue
        if val <= p :
            t_list.append(val)
    return len(t_list)
    