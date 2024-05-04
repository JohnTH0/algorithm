"""
둘만의 암호
https://school.programmers.co.kr/learn/courses/30/lessons/155652
lv 1
"""
import string

def solution(s, skip, index):
    
    # 문자열 리스트 변환
    s_list = list(s)
    skip_list = list(skip)
    
    # skip을 제외한 나머지 알파벳 리스트 선언
    alphabet_list = [i for i in string.ascii_lowercase]
    skip_alphabet_list = sorted(list(set(alphabet_list) - set(skip_list)))
    skip_alphabet_list_len = len(skip_alphabet_list)

    answer_list = []
    
    for char in s_list:
        new_index = skip_alphabet_list.index(char)
        new_char = skip_alphabet_list[(new_index+index) % skip_alphabet_list_len]
        answer_list.append(new_char)

    return "".join(answer_list)
