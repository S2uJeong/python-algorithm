"""
가장 긴 감소하는 부분 수열
같은 알고리즘에 dp를 업데이트 하는 조건문만 다르게 해줌
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = list(map(int,input().split()))

dp = [1] * (N+1) # 현재 idx까지의 최소 거리 (1)로 dp update

for i in range(N):
    for j in range(i):
        if nums[i] < nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))