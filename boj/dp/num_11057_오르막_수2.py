n = int(input())

# dp 테이블 선언 및 초기화
dp = [[0]*10 for _ in range(n+1)]

# n이 한 자리 수 일때 초기화
for i in range(0,10):
    dp[1][i] = 1

# n이 2~n 자릿 수 일때
for i in range(2,n+1):
    for j in range(10):
        if j == 0 :
            dp[i][j] = 1

        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]


print(sum(dp[n]) % 10007 )
