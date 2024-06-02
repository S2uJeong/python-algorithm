import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
tc = 1 # testCase number

def dijkstra(distance, maps):
    q = []
    distance[0][0] = maps[0][0]
    heapq.heappush(q, (maps[0][0], 0, 0))
    while q:
        dist, r, c = heapq.heappop(q)
        if distance[r][c] < dist:
            continue
        for dr,dc in directions:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N and distance[nr][nc] > maps[nr][nc] + dist :
                distance[nr][nc] = dist + maps[nr][nc]
                heapq.heappush(q, (distance[nr][nc], nr, nc))
    return distance[N-1][N-1]

while True:
    N = int(input().rstrip())
    if N == 0 :
        break
    maps = [list(map(int,input().split())) for _ in range(N)]
    distance = [[INF] * N for _ in range(N)]
    result = dijkstra(distance, maps)
    print(f'Problem {tc}: {result}')
    tc += 1



