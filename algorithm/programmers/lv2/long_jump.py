def solution(n):
    # 모든 자연수를 포함하기 위해 0부터 시작
    dp = [0] * (n + 1)
    # n == 1일때 자연수 1을 나타내는 방법의 개수는 하나 
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n] // 1234567

solution(3)