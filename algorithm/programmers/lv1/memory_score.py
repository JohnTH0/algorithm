"""
추억 점수
https://school.programmers.co.kr/learn/courses/30/lessons/176963
lv 1

name = ["may", "kein", "kain", "radi"]	
yearning = [5, 10, 1, 3]
photo = [
    ["may", "kein", "kain", "radi"],
    ["may", "kein", "brin", "deny"],
    ["kon", "kain", "may", "coni"]
    ]	
result = [19, 15, 6]
"""

def solution(name, yearning, photo):
    name_yearning_dict = dict(zip(name,yearning))
    answer = []
    for name_list in photo:
        memory_score = 0
        for name in name_list:
            if name in list(name_yearning_dict.keys()):
                memory_score += name_yearning_dict[name]
        answer.append(memory_score)

    return answer
