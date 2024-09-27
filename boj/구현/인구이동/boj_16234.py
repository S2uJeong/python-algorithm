"""
인구 이동이 다 됐는지 확인하는게 어려움,,
   - flag 사용 : 이중 for문을 계속 돌게하고, 변화된 값이 없으면 멈춘다.
전개하며 다음의 수와의 차이가 L ~ R 사이라면 다음 탐색으로 포함한다.
한 덩어리씩 처리한다고 생각하면 됨.
"""
from collections import deque
import sys
input = sys.stdin.readline


def update_map(chunks, chunks_sum):
    update_value = chunks_sum // len(chunks)
    for r,c in chunks:
        maps[r][c] = update_value

def bfs(start_r, start_c):
    chunks = [(start_r, start_c)]
    chunks_sum = maps[start_r][start_c]
    dQ = deque([(start_r, start_c)])
    visited[start_r][start_c] = True
    while dQ:
        r, c = dQ.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and L <= abs(maps[r][c] - maps[nr][nc]) <= R:
                dQ.append((nr,nc))
                visited[nr][nc] = True
                chunks.append((nr,nc))
                chunks_sum += maps[nr][nc]

    if len(chunks) == 1: # 시작점 외에 추가된 곳이 없으면 인구이동이 일어나지 않은것
        return False
    else:
        update_map(chunks, chunks_sum)
        return True


N, L, R = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

answer = 0
while True:
    change_flag = False
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i, j):
                    change_flag = True
    if not change_flag:
        break
    answer += 1

print(answer)
