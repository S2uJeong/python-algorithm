# https://school.programmers.co.kr/learn/courses/30/lessons/159993
# lv2
# 시간 복잡도  N = 2 * (100 * 100) = 20000
from collections import deque
def solution(maps):
    rows = len(maps)
    cols = len(maps[0])

    # 방향 정의 - 상,하,좌,우
    dr = [-1, 1, 0, 0]  # 행
    dc = [0, 0, -1, 1]  # 열

    def bfs(start, end):
        visited = [[False] * cols for _ in range(rows)]  # 방문 여부 리스트  - bfs는 처음 방문한 때가 최단거리이다.
        # 시작/레버 위치로 값으로 초기화 한다.
        dQ = deque([(start[0],start[1],0)])
        visited[start[0]][start[1]] = True
        # bfs 탐색
        while dQ:
            # 시작 위치에 대한 정보
            r,c,d = dQ.popleft()

            if r == end[0] and c == end[1]:
                return d

            for k in range(4):
                nr,nc =  r + dr[k], c + dc[k]
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and maps[nr][nc] != 'X':
                    visited[nr][nc] = True
                    dQ.append((nr, nc, d + 1))

        return 0

    # 시작,레버,출구 위치 찾기
    targets = [[0] for i in range(3)]
    for i in range(len(maps)):
        if maps[i].find('S') > -1:
            targets[0] = (i,maps[i].find('S'))
        if maps[i].find('L') > -1:
            targets[1] = (i,maps[i].find('L'))
        if maps[i].find('E') > -1:
            targets[2] = (i,maps[i].find('E'))

    res1 = bfs(targets[0],targets[1])
    res2 = bfs(targets[1],targets[2])

    if res1 and res2 :
        return res1 + res2
    else :
        return -1


print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))

