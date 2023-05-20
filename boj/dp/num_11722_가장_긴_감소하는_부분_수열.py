import sys
input = sys.stdin.readline

n = int(input())
input_list = list(map(int,input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if input_list[j] > input_list[i] :
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))