"""
횟수를 반복할수록 카드가 더해서 값이 커지는데, 그 눈덩이를 최소화 하려면
작은거끼리 더해서 덩어리를 작게 하는 방법이 있다.
"""
import sys
import heapq
input = sys.stdin.readline
N = int(input().rstrip())
nums = [int(input().rstrip()) for _ in range(N)]
# 문제풀이 시작
if N == 1:
    print(0)
else:
    heapq.heapify(nums)
    total_cost = 0

    while len(nums) > 1 :
        first = heapq.heappop(nums)
        second = heapq.heappop(nums)
        cost = first + second
        total_cost += cost
        heapq.heappush(nums, cost)

    print(total_cost)