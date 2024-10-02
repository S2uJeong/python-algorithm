"""
방향그래프, 시작점에서 다른 모든 정점으로의 최단 경로 구하기
다익스트라
1. 출발 노드 설정
2. 최단 거리 테이블 초기화
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용 계산
5. 3,4 반복
"""
import heapq
import sys
input = sys.stdin.readline

def cal_shortest_dist():
    INF = int(1e9)
    shortest_dist = [INF] * (V+1)
    shortest_dist[start_node] = 0
    hq = []
    heapq.heappush(hq, (0, start_node))

    while hq:
        dist, now = heapq.heappop(hq)

        if shortest_dist[now] < dist: # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            continue

        for nx, w in graph[now]:
            cost = dist + w # 현재 노드를 거쳐서 가는 비용 계산
            if cost < shortest_dist[nx]:
                shortest_dist[nx] = cost
                heapq.heappush(hq, (cost, nx))

    return shortest_dist

# 입력
V, E = map(int,input().split())
start_node = int(input().rstrip())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    fr, to, w = map(int,input().split())
    graph[fr].append((to, w)) # w는 거리 (가중치)
shortest_dist = cal_shortest_dist()

for i in range(1, len(shortest_dist)):
    if shortest_dist[i] >= int(1e9):
        print('INF')
    else:
        print(shortest_dist[i])
