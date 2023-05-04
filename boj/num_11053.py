import sys

n = int(input()) # 수열의 크기 입력
data = list(map(int,sys.stdin.readline().split())) # data 입력받아서 list화

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))