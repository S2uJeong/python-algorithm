"""
직사각형 범위만큼을 표기해주는 것이 관건
"""
from collections import deque
import sys
input = sys.stdin.readline

def check_quadrangle(start, end):
    # (0,2) , (4,4) 이면 (0,2) 0,3 1,2 1,3 2,2 2,3 3,2 (3,3)
    for r in range(start[0], end[0]):
        for c in range(start[1], end[1]):
            maps[r][c] = 1

def bfs(location):
    dQ = deque([location])
    count = 1

    while dQ :
        r,c = dQ.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and not maps[nr][nc]: # 색칠된 영역이 아니여야 함.
                dQ.append((nr,nc))
                maps[nr][nc] = 1
                count += 1
    return count


N,M,K = map(int,input().split())
maps = [[0] * M for _ in range(N)]
for _ in range(K):
    sc,sr,ec,er = map(int,input().split())
    check_quadrangle((sr,sc), (er,ec))

dr = [1,-1,0,0]
dc = [0,0,1,-1]

fragment = 0
amount = []
for r in range(N):
    for c in range(M):
        if not maps[r][c] :
            fragment += 1
            maps[r][c] = 1
            amount.append(bfs((r,c)))

print(fragment)
amount.sort()
for c in amount:
    print(c, end=' ')