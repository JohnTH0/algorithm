"""
신규 아이디 추천
https://school.programmers.co.kr/learn/courses/30/lessons/72410
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

길이의 변화 : 2->3->4->5->6->7
"""

from itertools import groupby
from collections import deque

def solution(new_id:str) -> str:
    new_id_list = list(new_id)
    
    # lv 1 & 2
    new_id_list = [char.lower() for char in new_id_list if char.isalpha() or char.isalnum() or char in ["-","_","."]]

    # lv 3 & 4
    new_id_list_deque = deque()
    for key, group in groupby(new_id_list):
        if key == '.':
            new_id_list_deque.append(key)
        else:
            new_id_list_deque.extend(list(group))

    if new_id_list_deque[0] == '.' :
        new_id_list_deque.popleft()

    if len(new_id_list_deque) == 0:
        new_id_list_deque = deque(["a"])

    if new_id_list_deque[-1] == '.' :
        new_id_list_deque.pop()
    
    # lv 5
    if len(new_id_list_deque) == 0:
        new_id_list_deque = deque(["a"])

    new_id_list_after = list(new_id_list_deque)

    # lv 6
    if len(new_id_list_after) >= 16:
        new_id_list_after = new_id_list_after[:15]

    if new_id_list_after[-1] == '.' :
        new_id_list_after.pop()

    # lv 7
    last_char = new_id_list_after[-1]
    if len(new_id_list_after) <= 2:
        while len(new_id_list_after) < 3:
            new_id_list_after.append(last_char)

    return "".join(new_id_list_after)

new_id = "=.="
result = "bat.y.abcdefghi"

solution(new_id)
"""
# 7단계만 수정
last_char = new_id_list_after[-1]
result_string = "".join(new_id_list_after).ljust(3,last_char)
ljust(len,char),rjust(len,char) 지정한 길이(len)보다 작을 경우,
len이 될 때까지 앞,뒤로 char를 추가, default char는 공백
"""


"""
정규식 풀이

import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    or
    new_id = new_id if len(new_id) > 3 else new_id + new_id[-1] * (3 - len(new_id))
    return st
"""