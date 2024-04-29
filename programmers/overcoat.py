"""
덧칠하기
https://school.programmers.co.kr/learn/courses/30/lessons/161989
lv 1

"""

def solution(n, m, section):
    # 칠하는 횟수
    count = 0
    
    # 시작 위치
    section_path = section[0]

    for target_num in section:
        # 시작위치에서 롤러 길이를 추가한 값(section_path도 칠해줘야 하므로 -1)이 target_path, 칠해야 하는 위치값보다 작으면
        # 시작위치에서 롤러 길이만큼 칠한 것으로 생각하여 위치를 이동, 이후 다시 비교
        if section_path + m - 1 < target_num:
            count += 1
            section_path = target_num

    # 마지막에 한 번 칠해야됨(위의 조건이 성립하지 않는 경우에 마지막 남은 칸을 한번 칠해야 하므로)
    count += 1

    return count

# 길이
n = 8
#한번에 칠하는 규칙
m = 4
section = [2, 3, 6]

print(solution(n, m, section))