"""
평범한 배낭 : 냅색문제
"""
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
crystals = [list(map(int,input().split())) for _ in range(N)]
dp = [0] * (K+1)

for w, v in crystals:
    for i in range(K, 0, -1):
        if i >= w:
            dp[i] = max(dp[i], dp[i-w] + v)

print(dp[K])