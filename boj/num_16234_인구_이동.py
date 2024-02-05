from collections import deque
N, L, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
union = [[-1]*N for _ in range(N)]

# 국경선 개방 여부 결정 함수
def bfs(r,c, idx):
    dQ = deque([(r,c)])
    summary = graph[r][c]
    cnt = 1
    unitied = []
    unitied.append((r,c))
    union[r][c] = idx

    while dQ:
        r,c = dQ.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < N and 0 <= nc < N and L <= abs(graph[nr][nc] - graph[r][c]) <= M and union[nr][nc] == -1 :
                dQ.append((nr, nc))
                union[nr][nc] = idx
                cnt += 1
                summary += graph[nr][nc]
                unitied.append((nr,nc))

    for r,c in unitied:
        graph[r][c] = summary//cnt
    return cnt

total_cnt = 0

while True:
    idx = 0
    for i in range(N):
        for j in range(N):
            if union[i][j] == -1:
                bfs(i,j,idx)
                idx += 1
    if idx == N*N:
        break
    total_cnt += 1

print(total_cnt)