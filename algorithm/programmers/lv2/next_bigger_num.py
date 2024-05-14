"""
다음 큰 숫자
https://school.programmers.co.kr/learn/courses/30/lessons/12911
lv 2
조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
"""

"""
review : Counter를 사용하지않고 bin(n).count를 해도 됨
search_n_one = bin(n).count('1')
"""

from collections import Counter
def solution(n):
    search_n_one = Counter(bin(n)[2:]).get("1")
    point = 1
    while True:
        target_num = n + point
        target_num_search_one = Counter(bin(target_num)[2:]).get("1")
        if search_n_one == target_num_search_one:
            break
        else:
            point += 1

    return target_num

n = 78
solution(n)