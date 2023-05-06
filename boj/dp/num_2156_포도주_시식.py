import sys

n = int(input())
dp = [0] * n

arrMount = list(map(int,([sys.stdin.readline().strip() for _ in range(n)])))

dp[0] = arrMount[0]

for i in range(1,n):
    if i == 1:
        dp[i] = arrMount[i-1] + arrMount[i]
    elif i == 2:
        dp[i] = max(dp[i-2], arrMount[i] + arrMount[i-2], arrMount[i-1] + arrMount[i])
    else :
        dp[i] = max(dp[i-1],dp[i-3] + arrMount[i-1] + arrMount[i],dp[i-2] + arrMount[i])

print(dp[-1])

# https://www.acmicpc.net/status?user_id=sj9802&problem_id=2156&from_mine=1