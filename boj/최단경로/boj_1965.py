"""
사이클이 없는 경우 -1 , 있으면 최소 거리로 return
- 단방향
- 간선이 0개일 수 있음 => -1

첫번째 시도  => 시간 초과
    bfs로 할 시, 덩어리가 여러개 일 수 있다는 점에서 고려해야 함.
    dfs를 통해 한 점을 시작점으로 잡고, 큐에서 시작점이 나올 때까지 bfs를 각각 돌리면?
    노드가 최대 400개 이므로 시도해본다.
두번째 시도
    dp[from][to] 최단거리 다 구해놓고, dfs 하며 미리 최단값 확인하고 경로 확인
    플루이드워셜 쓰면 노드 400개에 64_000_000 이므로 가능
"""
import sys
input = sys.stdin.readline

V,E = map(int,input().split())

# 특별처리
if E <= 1:
    print(-1)
    exit()

INF = int(1e9)
dp = [[INF] * (V+1) for _ in range(V+1)] # 최단 거리

for _ in range(E):
    f_node, t_node, dist = map(int,input().split())
    dp[f_node][t_node] = dist

# 플로이드-와샬
for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

# 최단 사이클 찾기
result = INF
for node in range(1,V+1):
    result = min(result, dp[node][node])

if result == INF :
    print(-1)
else : print(result)


def time_over():
    V, E = map(int, input().split())

    # 특별처리
    if E <= 1:
        print(-1)
        exit()

    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        f_node, t_node, dist = map(int, input().split())
        graph[f_node].append((t_node, dist))

    result = int(1e9)
    for start_node in range(1,V+1):
        visited = [False] * (V+1)
        dQ = deque([(start_node,0)]) # 일부러 방문 처리 안 한다.
        tmp_result = 0
        while dQ:
            now, dist = dQ.popleft()
            tmp_result += dist

            if now == start_node and visited[now]:
                result = min(result, tmp_result)

            for next, dist in graph[now]:
                if not visited[next]:
                    dQ.append((next,dist))
                    visited[next] = True

    if result == int(1e9):
        print(-1)
    else : print(result)