"""
https://www.acmicpc.net/problem/2480
"""

from collections import Counter
point_1, point_2, point_3 = input().split()
point_list = []
point_1, point_2, point_3 = int(point_1), int(point_2), int(point_3)
point_list = [point_1, point_2, point_3]

if len(set(point_list)) == 3:
    print(max(point_list) * 100)
elif len(set(point_list)) == 1:
    print(10000 + (max(point_list)) * 1000)
else:
    big_point = Counter(point_list).most_common(n=1)[0][0]
    print(1000 + (big_point * 100))
    