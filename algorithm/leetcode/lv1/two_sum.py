"""
07 두 수의 합
lv 1
"""

def solution(nums:list, target:int) -> list[int]:
    nums_dict = {}
    answer = []
    for i, num in enumerate(nums):
        nums_dict[num] = i 
    
    for i, num in enumerate(nums):
        if num > target :
            continue

        if target - num in nums_dict and not i == nums_dict[target - num]:
            target_list = [i, nums_dict[target - num]]

            if [nums_dict[target - num], i] in answer:
                continue

            answer.append(target_list)

    return answer

nums = [2,3,6,7,11,15]
target = 9
solution(nums, target)