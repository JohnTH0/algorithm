"""
키패드 누르기
https://school.programmers.co.kr/learn/courses/30/lessons/67256
lv 1
123
456
789
*0#
* 왼시작 # 오시작
"""

def solution(numbers:list, hand:str) -> str:
    left_path = [0,0]
    right_path = [2,0]
    result_str = ""
    init_keypad_dict = {
        "0" : [1,0],
        "1" : [0,3],
        "2" : [1,3],
        "3" : [2,3],
        "4" : [0,2],
        "5" : [1,2],
        "6" : [2,2],
        "7" : [0,1],
        "8" : [1,1],
        "9" : [2,1]
    }

    def cal_distance(now_path, target_path):
        now_x, now_y = now_path[0], now_path[1] 
        target_x, target_y = target_path[0], target_path[1]
        return abs(now_x - target_x) + abs(now_y - target_y)

    for target_num in numbers:
        if target_num in [1, 4, 7]:
            result_str += "L"
            left_path = init_keypad_dict[str(target_num)]
            continue
        elif target_num in [3, 6, 9]:
            result_str += "R"
            right_path = init_keypad_dict[str(target_num)]
            continue

        target_path = init_keypad_dict[str(target_num)]

        if cal_distance(left_path, target_path) > cal_distance(right_path, target_path):
            result_str += "R"
            right_path = init_keypad_dict[str(target_num)]
        elif cal_distance(left_path, target_path) < cal_distance(right_path, target_path):
            result_str += "L"
            left_path = init_keypad_dict[str(target_num)]
        else:
            if hand == "left" :
                result_str += "L"
                left_path = init_keypad_dict[str(target_num)]
            else:
                result_str += "R"
                right_path = init_keypad_dict[str(target_num)]

    return result_str

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
hand = "right"
solution(numbers,hand)