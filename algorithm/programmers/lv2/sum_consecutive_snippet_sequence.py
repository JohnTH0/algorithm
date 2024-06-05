"""
연속된 부분 수열의 합
https://school.programmers.co.kr/learn/courses/30/lessons/178870
lv 2
부분 수열의 합은 k입니다.
합이 k인 부분 수열이 여러 개인 경우 길이가 짧은 수열을 찾습니다.
길이가 짧은 수열이 여러 개인 경우 앞쪽(시작 인덱스가 작은)에 나오는 수열을 찾습니다.
"""
# lower_bound
# def solution(sequence, k):
#     L = len(sequence)
#     sequence = [0] + sequence
#     print(sequence)
#     for i in range(1, L+1):
#         sequence[i] = sequence[i-1] + sequence[i]
#     print(sequence)
#     for l in range(1, L + 1):
#         if sequence[-1] - sequence[-1 - l] < k:
#             continue
#         if sequence[l] - sequence[0] > k:
#             break
#         print(sequence)
#         s = 0
#         e = L - l

#         while s < e:
#             m = (s + e) // 2
#             if sequence[m+l] - sequence[m] >= k:
#                 e = m
#             else:
#                 s = m + 1

#         if sequence[s+l] - sequence[s] == k:
#             return [s, s + l - 1]
    
# two-pointer
def solution(sequence, k):
    n = len(sequence)

    max_sum = 0
    end = 0

    res = []
    for i in range(n):

        while max_sum < k and end < n:
            max_sum += sequence[end]
            end += 1

        if max_sum == k:
            res.append([i, end-1, end-1-i])

        max_sum -= sequence[i]

    res = sorted(res, key=lambda x: x[2])
    print(res)
    return res[0][:2]


# sequence = [2, 2, 2, 2, 2]
sequence = [1, 1, 1, 2, 3, 4, 5]
# k = 6
k = 5
print(solution(sequence, k))