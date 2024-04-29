"""
대충 만든 자판
https://school.programmers.co.kr/learn/courses/30/lessons/160586
lv 1
"""
def solution(keymap,targets):
    alphabet_dict = {}
    result_list = []
    
    for keymap_str in keymap:
        for idx, char in enumerate(keymap_str):
            if char not in alphabet_dict or idx < alphabet_dict[char]:
                alphabet_dict[char] = idx + 1

    for target in targets:
        score = 0
        alphabet_check = True
        for char in target:
            # 문자가 딕셔너리에 있는지 확인
            if char in alphabet_dict:
                # 있다면 해당 값을 합산
                score += alphabet_dict[char]
            else:
                alphabet_check = False
                break
        if alphabet_check:
            result_list.append(score)
        else:
            result_list.append(-1)
    return result_list

keymap = ["ABACD", "BCEFD"]
targets = ["ABCD","AABB","Z"]
result = [9, 4]

print(solution(keymap,targets))