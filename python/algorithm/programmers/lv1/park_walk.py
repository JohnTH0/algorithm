"""
공원 산책
https://school.programmers.co.kr/learn/courses/30/lessons/172928
lv 1
park = ["SOO","OOO","OOO"]
routes = ["E 2","S 2","W 1"]
result = [2,1]
"""
def solution(park, routes):
    # 시작점 찾기
    start_path = []
    for idx, start_loc in enumerate(park):
        split_str = [char for char in start_loc]
        if "S" in split_str:
            start_path = [idx,start_loc.index("S")]
            break
        else:
            continue

    # 이동 방향에 따른 좌표 변경
    directions = {"E": (0, 1), "W": (0, -1), "S": (1, 0), "N": (-1, 0)}

    for route in routes:
        op, steps = route.split()[0] , int(route.split()[1])
        next_row, next_col = start_path[0], start_path[1]
        for _ in range(steps):
            if 0 <= next_row + directions[op][0] < len(park) and 0 <= next_col + directions[op][1] < len(park[0]) and park[next_row + directions[op][0]][next_col + directions[op][1]] != "X":
                next_row += directions[op][0]
                next_col += directions[op][1]
            else:
                next_row = start_path[0]
                next_col = start_path[1]
                break
        start_path[0], start_path[1] = next_row, next_col
    return start_path

park = ["OSO","OOO","OXO","OOO"]
routes = ["E 2","S 2","W 1"]

print(solution(park,routes))
