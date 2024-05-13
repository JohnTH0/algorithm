"""
구명보트
https://school.programmers.co.kr/learn/courses/30/lessons/42885
lv 2
"""

def solution(people:list, limit:int) -> int:
    people.sort()
    len_people = len(people)
    count = 0 
    left, right = 0, len_people - 1
    while left <= right:
        # 마지막 선택된 인원
        if left == right:
            count +=1
            break
        # 보트에 탑승 가능한 경우
        if people[left] + people[right] <= limit:
            left += 1
        # 탑승할 수 없는 경우 가장 무거운 인원을 제외
        right -=1
        count +=1
    return count

people = [70, 50, 80, 50]
limit = 100
solution(people, limit)