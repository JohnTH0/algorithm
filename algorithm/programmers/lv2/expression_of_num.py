"""
숫자의 표현
https://school.programmers.co.kr/learn/courses/30/lessons/12924
lv 2
"""

def solution(n:int) -> int:
    count = 0
    list_n = [i+1 for i in range(n)]
    for i in range(len(list_n)):
        point = 0
        sum_result = 0
        while sum_result <= n:
            sum_result = sum(list_n[i:i + point])
            if sum_result < n:
                point +=1
            elif sum_result > n:
                break
            else:
                count += 1
                break

    return count
n = 15
solution(n)