"""
https://school.programmers.co.kr/learn/courses/30/lessons/120956
옹알이 (1)
"aya", "ye", "woo", "ma"
"""

def solution(babbling:list) -> int:
    # 횟수를 세기 위한 변수 선언
    count = 0
    """
    중첩 for 문을 사용하여 각 단어를 구성하는 알파벳을 하나씩 추가하고
    추가하는 도중 해당하는 말할 수 있는 단어 안에 포함되는 경우 초기화
    """
    for bab in babbling:
        bab_check_str = ""
        for i in range(len(bab)):
            bab_check_str += bab[i]
            if bab_check_str in ["aya", "ye", "woo", "ma"]:
                bab_check_str = ""

        if bab_check_str == "":
            count +=1

    return count

babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
solution(babbling)