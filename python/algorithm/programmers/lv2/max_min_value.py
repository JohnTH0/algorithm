"""
최댓값과 최솟값
https://school.programmers.co.kr/learn/courses/30/lessons/12939
lv 2
"""
def solution(s):
    list_s = list(map(int, s.split()))
    return "{} {}".format(min(list_s),max(list_s))
            
s = "-1 -2 -3 -4"
solution(s)