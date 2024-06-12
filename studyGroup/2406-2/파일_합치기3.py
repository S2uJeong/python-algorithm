import heapq
import sys
input = sys.stdin.readline
T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())
    nums = list(map(int,input().split()))

    heapq.heapify(nums)
    result = 0
    while len(nums) > 1 :
        file1 = heapq.heappop(nums)
        file2 = heapq.heappop(nums)
        sum_file = file1 + file2
        heapq.heappush(nums, sum_file)
        result += sum_file

    print(result)

