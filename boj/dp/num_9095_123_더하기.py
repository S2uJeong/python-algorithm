memo = [0] * 11
memo[1] = 1
memo[2] = 2
memo[3] = 4

for i in range(4,11):
    memo[i] = sum(memo[i-3:i])

t = int(input())
for i in range(t):
    print(memo[int(input())])