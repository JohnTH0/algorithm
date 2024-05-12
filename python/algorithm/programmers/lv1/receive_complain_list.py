"""
신고 결과 받기
https://school.programmers.co.kr/learn/courses/30/lessons/92334
lv 1
"""
def solution(id_list, report, k):
    id_dict = {id : i for i, id in enumerate(id_list)}
    id_2d_list = [[0] * len(id_list) for _ in range(len(id_list))]
    report_list = list(set(report))
    
    """
    신고리스트를 순회하면서 누가 누구를 신고했는지 확인하여 추가
    [[0, 1, 0, 1], [0, 0, 0, 1], [1, 1, 0, 0], [0, 0, 0, 0]]
    첫번째 리스트 부터 id_list순서대로 신고한 유저에 1
    """
    for complain in report_list:
        give, take = complain.split()
        give_key, take_key = id_dict[give], id_dict[take]
        id_2d_list[give_key][take_key] += 1

    """
    인덱스로 리스트를 변경하여 각 튜플별 신고한 유저 확인
    [(0, 0, 1, 0), (1, 0, 1, 0), (0, 0, 0, 0), (1, 1, 0, 0)]
    무지를 신고한 사람 = appeach
    """
    id_2d_col_list = list(zip(*id_2d_list))

    result_complain = [0] * len(id_list)
    
    # 신고받은 횟수가 k 이상인 경우 해당 유저를 신고한 인원들 확인 
    for take_complain in id_2d_col_list:
        take_complain_result = sum(take_complain)
        if take_complain_result >= k:
            for i in range(len(result_complain)):
                if take_complain[i] == 1:
                    result_complain[i] +=1

    return result_complain
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

solution(id_list, report, k)