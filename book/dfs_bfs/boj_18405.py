import sys
from collections import deque
input = sys.stdin.readline
# ======== 입력
N, K = map(int,input().split())
maps = [] # 전체 보드 정보
data = [] # 바이러스 정보

for i in range(N):
    maps.append(list(map(int,input().split())))
    for j in range(N):
        if maps[i][j] != 0 :
            # (virus, s, x, y)
            data.append((maps[i][j],0,i,j))
data.sort()
q = deque(data)

S,X,Y = map(int,input().split())
# ======= 문제풀이
dr = [-1,1,0,0]
dc = [0,0,-1,1]

# 1초마다 상하좌우 전파되며, 바이러스 순번이 낮은것이 우선 전파된다.
# 바이러스 값이 0일때만 전파 가능하다.

while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때 까지 반복
    if s == S :
        break
    for k in range(4):
        nx = x + dr[k]
        ny = y + dc[k]
        if nx >= 0 and nx < N and ny >= 0 and ny < N and maps[nx][ny] == 0:
            maps[nx][ny] = virus
            q.append((virus, s+1, nx, ny))

print(maps[X-1][Y-1])