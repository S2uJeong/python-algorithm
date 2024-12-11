"""
### 알고리즘 유형 고민
움직이는건 무조건 최단 경로로 가야 하는데, 그 중에서도 제일 긴거리를 찾아야 하므로 모든 노드-노드 간의 거리를 구해주어야 합니다.
최단 경로를 구해야 하는 문제이므로 bfs를 사용합니다.

### 시간 복잡도 고민
노드의 개수가 최대 50 * 50 = 2500 이며
BFS의 시간복잡도는 O(노드 개수 V + 간선 개수 E)
for문이 모든 노드를 한 번씩 출발점으로 지정하도록 되어 있기 때문에 감안하면 O(V * (V + E))
따라서 2500×O(V+E)=2500×O(12500)=O(31,250,000)
최악의 경우 O(V^3)이 나옵니다.

### 개선점
for문에서 첫 시작이 땅일 때만 돌리도록 해서 최대한 줄여 타임아웃이 발생하지 않았습니다.
"""
from collections import deque
def bfs(maps, start_r, start_c):
    global result

    dr = [0,0,-1,1]
    dc = [-1,1,0,0]

    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    dQ = deque([(start_r,start_c)])
    visited[start_r][start_c] = 1
    distance = 0

    while dQ:
        for _ in range(len(dQ)):
            crt_r, crt_c = dQ.popleft()
            for k in range(4):
                nr = crt_r + dr[k]
                nc = crt_c + dc[k]
                if 0 <= nr < len(maps) and 0 <= nc < len(maps[0]) and not visited[nr][nc] and maps[nr][nc] == 'L' :
                    dQ.append((nr,nc))
                    visited[nr][nc] = 1
        distance += 1

    result = max(result, distance - 1)

N,M = map(int,input().split())
maps = list(input() for _ in range(N))
result = 0

for i in range(len(maps)):
    for j in range(len(maps[i])):
        if maps[i][j] == 'L':
            bfs(maps, i, j)

print(result)

