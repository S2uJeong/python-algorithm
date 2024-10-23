"""
증가하는 부분 수열의 수의 합이 가장 큰 것을 출력

합과 길이는 비례하지 않음.
dfs를 사용하면 깊이가 최대 1,000이라 2^1000이라 불가
dp를 사용한다.
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = list(map(int,input().split()))
dp = nums[:]

for dp_idx in range(1,N):
    for num_idx in range(dp_idx):
        if nums[num_idx] < nums[dp_idx]:
            dp[dp_idx] = max(dp[dp_idx], dp[num_idx] + nums[dp_idx])

print(max(dp))