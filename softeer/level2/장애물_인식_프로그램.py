from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip())
maps = [input().rstrip() for _ in range(N)]

dr = [0,0,-1,1]
dc = [-1,1,0,0]
result = []
visited = [[False] * N for _ in range(N)]

def bfs(start_point_r, start_point_c): # 최초 장애물 지점 발견 시 dfs 발동
    dQ = deque()
    dQ.append((start_point_r, start_point_c))
    count = 1  # 블럭 안에 포함된 point의 갯수를 샌다.

    while dQ:
        r, c = dQ.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and maps[nr][nc] == '1':
                dQ.append((nr,nc))
                visited[nr][nc] = True
                count += 1

    result.append(count)

for i in range(N):
    for j in range(N):
        if visited[i][j] == False and maps[i][j] == '1' :
            visited[i][j] = True
            bfs(i,j)

print(len(result))
result.sort()
for value in result:
    print(value)