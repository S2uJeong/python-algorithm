"""
매 초마다 번호가 낮은 종류의 바이러스가 먼저 증식한다.
"""
from collections import deque
import sys
input = sys.stdin.readline

def bfs(virus_list):
    dc = [0, 0, 1, -1]
    dr = [-1, 1, 0, 0]

    dQ = deque(virus_list)

    while dQ:
        virus_kind, second, r, c = dQ.popleft()
        if second >= S:
            return
        for k in range(len(dc)):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and maps[nr][nc] == 0:
                maps[nr][nc] = virus_kind
                dQ.append([virus_kind, second +1, nr, nc])


N, K = map(int,input().split())
maps = []
virus_list = [] #(바이러스 종류, 시간, r,c)

for i in range(N):
    maps.append(list(map(int,input().split())))
    for j in range(N):
        if maps[i][j] != 0 :
            virus_list.append([maps[i][j], 0, i, j])

S,X,Y = map(int,input().split())

virus_list.sort()  # 작은 값의 바이러스가 먼저 퍼지는 것을 보장함.
bfs(virus_list)

# 주의점 : input r,c는 (1,1) 부터 시작되는 인덱스 표기법이다
print(maps[X-1][Y-1])