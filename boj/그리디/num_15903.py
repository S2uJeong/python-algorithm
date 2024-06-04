"""
아이디어 : 작은 숫자끼리 최대한 더해야 전체 수가 커지지 않는다.
최소힙을 사용해서 합체 수동안 매번 작은 수를 골라 더해서 추가해준 뒤, 전체 sum을 구한다.
"""
import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

heapq.heapify(nums)
for _ in range(M):
    first = heapq.heappop(nums)
    second = heapq.heappop(nums)
    tmp = first + second
    for _ in range(2):
        heapq.heappush(nums, tmp)

print(sum(nums))
