"""
n가지 종류의 동전으로 합으로 k원으로 만든다. (개수는 최소로, 동전은 중복사용 가능)
"""
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
coins = [int(input().rstrip()) for _ in range(N)]
dp = [10001] * (K+1)
dp[0] = 0

for sum in range(1,K+1):
    for cn in coins:
        if sum < cn : continue
        dp[sum] = min(dp[sum], dp[sum-cn] + 1)

if dp[K] == 10001:
    print(-1)
else:
    print(dp[K])


