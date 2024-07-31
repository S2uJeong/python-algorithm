"""
dp로 처음부터 해당 idx까지의 합을 구해놓고,
범위가 주어졌을 때 dp[j] - dp[i] 해서 푼다.

유의점
- dp[i]가 마이너스 일 때 값이 올바르지 않음.  => if문으로 예외처리
"""

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split())) # 앞 쿠션
dp = [0] * (N+1) # 앞 쿠션
for i in range(1,len(dp)):
    dp[i] = dp[i-1] + nums[i-1]

for _ in range(int(input())):
    s,e = map(int,input().split())
    print(dp[e] - dp[s-1])

