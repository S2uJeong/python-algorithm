import sys
import heapq
input = sys.stdin.readline

city = int(input().rstrip())
bus = int(input().rstrip())
# 그래프 입력 : s - (e으로 가는데, dist(거리,비용))
graph = [[] for _ in range(city + 1)] # city 번호: 1 ~ city
for i in range(bus):
    s,e,dist = map(int,input().split())
    graph[s].append((e,dist))
# 문제
S, E = map(int,input().split())
INF = 1e9
distance = [INF] * (city + 1)

# 다익스트라
def dijkstra(S):
    # 시작지점 초기화
    distance[S] = 0
    # 최소힙 정의
    q = []
    heapq.heappush(q,(0,S)) # 거리, 노드
    # 시작
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next,d in graph[now]:
            cost = dist + d
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost,next))

dijkstra(S)
print(distance[E])
