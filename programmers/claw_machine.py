"""
크레인 인형뽑기 게임
https://school.programmers.co.kr/learn/courses/30/lessons/64061
lv 1
"""
def solution(board:list, moves:list):
    bucket = []
    count = 0
    board_col_list = [list(i) for i in zip(*board)]

    def target_doll_check(line):
        target_line = board_col_list[line-1]
        target_doll = next(filter(lambda x: x != 0, target_line),0)
        if target_doll == 0:
            return 0
        target_doll_index = target_line.index(target_doll)
        target_line[target_doll_index] = 0

        return target_doll
    
    for line in moves:
        target_doll = target_doll_check(line)
        if target_doll == 0:
            continue

        bucket.append(target_doll)

        if len(bucket) >= 2:
            if bucket[-2] == bucket[-1]:
                count +=1
                del bucket[-2:]
    return count * 2
        

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
result = 4
solution(board, moves)