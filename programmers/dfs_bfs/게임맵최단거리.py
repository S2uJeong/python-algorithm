"""
https://school.programmers.co.kr/learn/courses/30/lessons/1844
"""
from collections import deque
def solution(maps):
    # n, m 초기화
    n = len(maps)
    m = len(maps[0])
    # 필요한 자료구조 정의
    dQ = deque()
    visited = [[False] * m for _ in range(n)]
    # 시작점 정보
    dQ.append((0,0))
    visited[0][0] = True
    # 방향 초기화
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    cnt = 0 # 걸음 수
    while dQ :
        r,c = dQ.popleft()
        # print(f'dQ.pop : maps[{r}][{c}]')
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if (0 <= nr < n and 0 <= nc < m and not visited[nr][nc]
                    and maps[nr][nc] == 1): # 🔴point1 : 벽이 아닌곳 and 먼저 도착한 경우가 있으면 기본 입력값이었던 1이 아닐것이므로 가장 빠른길을 보장하주는 조건
                dQ.append((nr,nc))
                # print(f'방문한 곳 : maps[{nr}][{nc}] ,', end = ' ')
                visited[nr][nc] = True
                maps[nr][nc] = maps[r][c] + 1   # 🔴point2 전 값에서 1 더해주므로써 cnt를 해주며, point1의 조건식을 뒷받침한다.
                # print(maps)
    if maps[n-1][m-1] == 1 : #문제 정의상 도달하지 못했으면 길을 표현하는 기본값인 1의 값을 가진다.
        return -1
    return maps[n-1][m-1]

