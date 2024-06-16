import heapq
import sys
input = sys.stdin.readline

def dijkstra(start, graph, n):
    distances = [1e9] * (n+1)
    distances[start] = 0
    pq = [(0,start)]
    heapq.heapify(pq)

    while pq:
        cur_dis, node = heapq.heappop(pq)
        if cur_dis > distances[node]:
            continue
        for next, value in graph[node]:
            distance = cur_dis + value
            if distance < distances[next]:
                distances[next] = distance
                heapq.heappush(pq, (distance, next))

    return distances

T = int(input().rstrip())
for _ in range(T): # testCase
    n,m,t = map(int,input().split()) # 교차로, 도로, 목적지후보
    s,g,h = map(int,input().split()) # 출발지, 지난 노드1,2
    # graph 입력
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        node1, node2, distant = map(int,input().split())
        graph[node1].append([node2, distant])
        graph[node2].append([node1, distant])
    # 도착지 후보
    point_list = [int(input().rstrip()) for _ in range(t)]

    # 🔴 출발지를 [출발지,중간지점1,중간지점2]로 각각 설정한 다익스트라 최단경로 리스트를 만든다.
    dist_from_s = dijkstra(s, graph, n)
    dist_from_g = dijkstra(g, graph, n)
    dist_from_h = dijkstra(h, graph, n)

    result = []

    for point in point_list:
        path_s_g_h = dist_from_s[g] + dist_from_g[h] + dist_from_h[point]
        path_s_h_g = dist_from_s[h] + dist_from_h[g] + dist_from_g[point]

        # 🔴 g,h를 지난 건지 경로의 길이로 조건했을 때 알 수 있는 이유 : 최단경로로만 갔다고 조건되어 있고, 그 길 도중 g,h가 있는지 확인하라고 했으므로
        if dist_from_s[point] == min(path_s_g_h, path_s_h_g):
            result.append(point)

    if len(result) > 0 :
        result.sort()
        for val in result:
            print(val, end=' ')
        print()