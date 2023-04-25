n = int(input())

dp = [[0]*10 for _ in range(n+1)]

dp[1][0] = 0
for i in range(1,10):
    dp[1][i] = 1

for i in range(2,n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = 0

        if j == 9:
            dp[i][j] = 1

        else:
            dp[i][j] = 2

print(sum(dp[n]) % 1000000000)