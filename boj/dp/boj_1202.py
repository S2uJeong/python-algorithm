"""
보석도둑
: 그리디
"""
import heapq
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
crystal_info = [list(map(int,input().split())) for _ in range(N)]
bags = [int(input().rstrip()) for _ in range(K)]
picked_crystal_price = []
result = 0

crystal_info.sort()
bags.sort()

for i in range(len(bags)):
    while crystal_info and crystal_info[0][0] <= bags[i]:
        heapq.heappush(picked_crystal_price, -crystal_info[0][1])
        heapq.heappop(crystal_info)
    if picked_crystal_price:
        result -= heapq.heappop(picked_crystal_price)
print(result)