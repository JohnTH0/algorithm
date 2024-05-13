"""
09 세수의 합
lv 2
"""

def solution(nums:list) -> list:
    # 정렬
    nums.sort()
    print(nums)
    list_answer = []

    len_nums = len(nums)
    # 세 수의 합 이므로 첫 점을 i로 나머지 두 점을 양쪽끝에서부터 줄여 나가기 시작
    # range - 2인 이유는 기존 인덱스를 선언시 i - 1, 여기에 포인터가 세개이므로
    for i in range(len_nums - 2):
        # 중복값 조회
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum_result = nums[i] + nums[left] + nums[right]
            if sum_result < 0:
                left +=1
            elif sum_result > 0:
                right -= 1
            else:
                answer = [nums[i], nums[left], nums[right]]
                list_answer.append(answer)

                # 각 포인터의 다음 값에 같은 값이 있는 경우 이동
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[left - 1]:
                    right -= 1
                # 포인터 이동
                left += 1
                right -= 1

nums = [-1, 0, 1, 2, -1, -4]
solution(nums)