"""
1. 음식물 좌표를 담은 자료구조에 in으로 찾아서 deque에 넣는 방법
2. 이중리스트를 통해 T/F로 표시한 뒤, 이동 좌표에 해당 하는 인덱스에 대해서만 update
2번이 탐색 범위가 매번 상하좌우 4번이라 성능적으로 좋을것
"""
import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
trash_map = [[False] * M for _ in range(N)] # 쓰레기가 없거나, 이미 탕색한거면 False, 더할 쓰레기 대상이면 True
# trash_map에 쓰레기 True로 표시
for _ in range(K):
    r,c = map(int, input().split())
    trash_map[r-1][c-1] = True # input idx : 1~N , my idx : 0 ~ N-1

dc = [-1, 1, 0, 0]
dr = [0, 0, 1, -1]
def bfs(i,j):
    cnt = 0
    dQ = deque()
    dQ.append([i,j])
    trash_map[i][j] = False
    while dQ:
        r, c = dQ.popleft()
        cnt += 1
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and trash_map[nr][nc] == True:
                trash_map[nr][nc] = False
                dQ.append([nr, nc])
    return cnt

result = 0
for i in range(len(trash_map)):
    for j in range(len(trash_map[i])):
        if trash_map[i][j] == True:
            cnt = bfs(i,j)
            result = max(result, cnt)
print(result)