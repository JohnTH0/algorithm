"""
체육복
https://school.programmers.co.kr/learn/courses/30/lessons/42862
lv 1
"""

def solution(n:int, lost:list, reserve:list):
    # 여분을 가지고 있지만 자기자신이 잃어버린 학생
    lost_reserve_intersection_list = set(lost) & set(reserve)
    lost = set(lost) - lost_reserve_intersection_list
    reserve = list((set(reserve) - lost_reserve_intersection_list))

    # 전체 학생
    all_student_list = set([i+1 for i in range(n)])

    # 전체 학생 - 잃어버린 학생
    lost_all_student_list = list(all_student_list - lost)
    
    # 여분이 있는 학생리스트를 loop해서 앞뒤로 전체-잃어버린 학생 리스트에서 확인
    for reserve_student in reserve:
        if not reserve_student - 1 in lost_all_student_list and reserve_student - 1 > 0:
            lost_all_student_list.append(reserve_student - 1)
        elif reserve_student + 1 not in lost_all_student_list and reserve_student + 1 <= n:
            lost_all_student_list.append(reserve_student + 1)
    return len(lost_all_student_list)

# 전체학생
n = 30
# 잃어버린 학생
lost = [2, 4]
# 여분 학생
reserve = [3]
solution(n, lost, reserve)