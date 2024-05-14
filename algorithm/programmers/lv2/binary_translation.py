"""
이진 변환 반복하기
https://school.programmers.co.kr/learn/courses/30/lessons/70129
result = [횟수, 제거한 0의 개수]
x의 모든 0을 제거합니다.
x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꿉니다.
"""

def solution(s:list) -> list:
    count = 0
    del_zero = 0
    while True:
        list_s = list(s)
        count_zero = list_s.count("0")
        del_zero += count_zero
        s = bin(len("".join([num for num in list_s if num != "0"])))[2:]
        count += 1
        if s =="1":
            break
    return [count, del_zero]

s = "110010101001"
result = [3,8]
solution(s)