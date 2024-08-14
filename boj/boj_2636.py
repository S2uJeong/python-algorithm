"""
치즈 모양의 가장자리부터 치즈가 없어지는데, (치즈가 다 없어지는데 걸리는 시간, 모두 녹기 한 시간전에 남아 있는 치즈 칸의 개수)를 구하라

1. 이어진 치즈 덩어리 별로 물체를 인식한다 (bfs로 이어진 곳을 찾는다. Dq가 끝나면 해당 map을 가지고 물체 없애기를 시작한다.
2. 해당 물체가 있는 곳을 기준으로, 바깥에서 1 차이나는 곳들을 전부 없앤다.

---
1. 탐색을 0에서 1로 조회하는 순간 그 치즈는 녹는다.
2. 치즈를 녹였으면 더 이상 그 큐는 인접 탐색을 이어나가지 않는다.
"""
import sys
from collections import deque
input = sys.stdin.readline
# 치즈 한 덩이 찾기
def change_cheese_per_one_time(maps, start_point):
    visited = [[False] * M for _ in range(N)]
    turn_count = 0
    dr = [0,0,-1,1]
    dc = [-1,1,0,0]
    dQ = deque([start_point])
    while dQ:
        r,c = dQ.popleft()
        for k in range(len(dr)):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] :
                visited[nr][nc] = True
                if maps[nr][nc] == 1 :
                    maps[nr][nc] = 0
                    turn_count += 1
                elif maps[nr][nc] == 0:
                    dQ.append((nr,nc))

    return turn_count

N,M = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]

turn_count = 0
time = 0
while True:
    tmp_count = change_cheese_per_one_time(maps, (0,0))
    if tmp_count == 0 :
        break
    turn_count = tmp_count
    time += 1

print(time)
print(turn_count)