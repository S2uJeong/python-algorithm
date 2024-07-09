"""
시간제한이 0.25이므로 재귀가 아닌 DP를 통해 풀이함.

피보나치 수열 특성상 n = 0,1 일때 처리를 잘 해줘야함
"""

T = int(input())
for _ in range(T):
    N = int(input())
    if not N:  # 0일 때 처리
        print(1, 0)
        continue
    if N == 1:  # 1일 때 처리
        print(0, 1)
        continue
    # 일반 풀이 시작
    dp = [[0, 0] for _ in range(N + 1)]  # 인덱스로 호출된 n 표기, dp[n][0] : 0 카운트 값
    # 0,1일 때 초기화
    dp[0][0] = 1
    dp[1][1] = 1

    for i in range(2, N + 1):
        dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
        dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

    print(dp[N][0], dp[N][1])
