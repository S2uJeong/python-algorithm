n = int(input())
arr = list(map(int, input().split()))
memo = [0] * 100

memo[0] = arr[0]
memo[1] = arr[1]
for i in range(2,n):
    memo[i] = max(memo[i-1], memo[i-2]+arr[i])

print(memo[n-1])