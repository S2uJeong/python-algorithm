def max_subarray_sum_prefix(arr):
    n = len(arr)
    if n == 0:
        return 0

    # 누적합 배열 계산
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]

    max_sum = -float('inf')
    min_prefix_sum = 0

    for i in range(1, n + 1):
        max_sum = max(max_sum, prefix_sum[i] - min_prefix_sum)
        min_prefix_sum = min(min_prefix_sum, prefix_sum[i])

    return max_sum



import sys
input = sys.stdin.read
data = input().split()

index = 0
results = []

while index < len(data):
    N = int(data[index])
    if N == 0:
        break

    profits = []
    for i in range(1, N + 1):
        profits.append(int(data[index + i]))

    results.append(max_subarray_sum_prefix(profits))

    index += N + 1

for result in results:
    print(result)


