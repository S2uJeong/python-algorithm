import sys
input = sys.stdin.readline

N, K = map(int,input().split())
nums = list(map(int,input().split()))


stack_sum = [0]
cur_sum = []
tmp_sum = 0
answer = -100 * K

for i in range(N):
    tmp_sum += nums[i]
    stack_sum.append(tmp_sum)

for i in range(N-K+1):
    range_sum = stack_sum[i+K] - stack_sum[i]
    cur_sum.append(range_sum)
    if answer < range_sum:
        answer = range_sum

print(answer)

