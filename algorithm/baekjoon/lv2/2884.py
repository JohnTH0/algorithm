"""
https://www.acmicpc.net/problem/2884
"""

H, M = input().split()
H, M = int(H), int(M) - 45

if M < 0:
    M = 60 - abs(M)
    H -= 1
    
    if H < 0:
        H = 23
print("{} {}".format(H, M))