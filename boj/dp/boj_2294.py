"""
- 조건 : 동전의 가치 합이 K
- 목표 : 동전의 개수가 MIN

동전의 종류가 100개 이하라 경우의 수가 너무 많음. 따라서 DP를 사용해서 풀어낸다.
DP
- idx : 0 ~ K 의 금액을 나타낸다. ( k <= 10,000)
- val : 해당 금액을 만들기 위해 사용된 동전의 개수를 나타낸다.

DP 리스트를 돌며 해당 idx에 해당하는 금액을 만드는 것에 대해 탐색 시작
    해당 금액에서 동전 리스트를 돌며 min(dp[i - coin] + 1 , dp[i])를 실시한다.

K * N 의 시간 복잡도가 소요 된다. = 10,000 * 100 = 1,000,000
제한 시간이 1초이므로 가능하다.

항상 최선의 최단 경로를 찾는 방법도 사용할 수 있나?
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


