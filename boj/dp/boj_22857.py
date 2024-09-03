"""
부분 수열 중 가장 긴 길이를 출력하라
수열의 길이 : 1 ~ 50,000 / K : 1 ~ 100

dp[i][j]: i번째까지 고려했을 때, j개의 홀수를 제거했을 때 얻을 수 있는 가장 긴 짝수 연속 부분 수열의 길이.
"""
def longest_even_dp(nums,N,K):
    dp = [[0] * (K+1) for _ in range(N+1)]
    result = 0

    for i in range(1, N+1):
        for j in range(K+1):
            if nums[i-1] % 2 == 0 :
                dp[i][j] = dp[i-1][j] + 1
            else:  # 홀수인 경우
                if j > 0 : # j 가 삭제 카운트이므로 0 이상일 때만 삭제 가능
                    dp[i][j] = dp[i-1][j-1]

            # dp[i][j] = max(dp[i][j], dp[i-1][j])
            result = max(result, dp[i][j])

    return result


N, K = map(int,input().split())
nums = list(map(int,input().split()))
print(longest_even_dp(nums, N, K))
