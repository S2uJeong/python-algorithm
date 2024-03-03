"""
https://codeup.kr/problem.php?id=1512
"""
from collections import deque
m = int(input())
graph =  [[0] * m for _ in range(m)]
visited = [[False] * m for _ in range(m)]
dQ = deque()

str_r, str_c = map(int, input().split())
str_r, str_c = str_r-1, str_c-1
visited[str_r][str_c] = True
graph[str_r][str_c] = 1
dQ.append((str_r,str_c,1))

dr = [-1,1,0,0]
dc = [0,0,-1,1]

while dQ:
    r,c,value = dQ.popleft()
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if nr >= 0 and nr < m and nc >= 0 and nc < m and not visited[nr][nc]:
            graph[nr][nc] = value+1
            visited[nr][nc] = True
            dQ.append((nr,nc, value+1))

for i in range(m):
    for j in range(m):
        print(graph[i][j], end = ' ')
    print()


