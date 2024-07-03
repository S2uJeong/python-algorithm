"""
보석도둑 : 오토에버 2번 문항 비슷한 문제
"""
import sys
input = sys.stdin.readline
import heapq

N, K = map(int, input().split())
crystals = []
for _ in range(N):
    M, V = map(int,input().split())
    crystals.append((M,V))
bags = [int(input().rstrip()) for _ in range(K)]

def calulate_max_value(N, crystals, bags):
    # 보석과 가방을 각각 정렬
    crystals.sort() # 무게 오름차순
    bags.sort() # 무게 오름차순

    max_value = 0
    possible_crystals = []

    j = 0 # 보석 순번
    for bag in bags:
        while j < N and crystals[j][0] <= bag:
            heapq.heappush(possible_crystals, -crystals[j][1])  # 가격을 힙에 추가 (음수로) - 가격 내림차순
            j += 1
        if possible_crystals:
            max_value += -heapq.heappop(possible_crystals)  # 가장 큰 가격을 더함

    return max_value

def time_over(N, crystals, bags):
    dp = [0] * K # 해당 가방 무게에서 담을 수 있는 최대 보석의 가치
    visited = [False] * N # 이전 단게에서 선택된 보석은 담을 수 없다.

    bags.sort()
    crystals.sort(key = lambda x: (x[0], -x[1])) # 무게 오름차순, 가치 내림차순

    for i in range(len(bags)): # val : bag이 담을 수 있는 최대 무게
        for j in range(len(crystals)): # 보석 무게 : crystals[j][0], 보석 가치 : crystals[j][1]
            if crystals[j][0] > bags[i]:
                break
            if not visited[j] and dp[i] < crystals[j][1] :
                dp[i] = crystals[j][1]
                visited[j] = True
                break

    return sum(dp)


print(calulate_max_value(N, crystals, bags))