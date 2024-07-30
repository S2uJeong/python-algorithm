"""
무작위로 나열된 병사 중 특정 인원을 제외하여 전투력이 내림차순으로 정렬되도록 하되, 제외 되는 인원을 최소화 하라

## 가장 증가하는 부분 수열, dp 이용
- 해당 병사를 빼느냐 안 빼느냐에 따라서 dp를 업데이트 한다.
- 병사를 빼면, 앞의 값으로 update하고 안 빼면 확인해서
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
powers = list(map(int,input().split()))
dp = [1] * N

for i in range(1,N):
    for j in range(i):
        if powers[i] < powers[j] :
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))