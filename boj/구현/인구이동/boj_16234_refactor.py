import sys
from collections import deque
input = sys.stdin.readline

dr = (0,0,1,-1)
dc = (1,-1,0,0)

def bfs(sr,sc):
    population = maps[sr][sc]
    visited[sr][sc] = day
    today_visited_area = [(sr,sc)]
    for r,c in today_visited_area:
        for k in range(4):
            nr,nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] < day and L <= abs(maps[r][c] - maps[nr][nc]) <= R:
                visited[nr][nc] = day
                population += maps[nr][nc]
                today_visited_area.append((nr,nc))

    if len(today_visited_area) > 1:
        avg = population // len(today_visited_area)
        for r,c in today_visited_area:
            maps[r][c] = avg
            candidate.append((r,c))

N, L, R = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * N for _ in range(N)] # 방문일자를 value로 가진다.
# 체스판처럼 체크
candidate = deque([(r,c) for r in range(N) for c in range(r % 2, N, 2)])

day = 0
while candidate:
    for _ in range(len(candidate)):
        r,c = candidate.popleft()
        if visited[r][c] < day:
            bfs(r,c)
    day += 1

print(day-1)