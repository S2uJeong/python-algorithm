"""
얼음 조각 문제처럼 덩어리를 map에서 찾아서 그 수를 반환한다.
시간제한 1초, 테스트 케이스 있음,  1<= N,M <= 50
"""
from collections import deque
T = int(input().rstrip())
def check_one_chunk(maps, r,c):
    dQ = deque([(i,j)])
    dr = [0,0,-1,1]
    dc = [1,-1,0,0]
    while dQ:
        r, c = dQ.popleft()
        for k in range(len(dr)):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and not maps[nr][nc]:
                dQ.append((nr,nc))
                maps[nr][nc] = 1

    return maps

for _ in range(T):
    # 선언 및 초기화
    M,N,K = map(int,input().split())
    maps = [[2] * M for _ in range(N)]  # 0 : 배추,  1: 배추 였는데, 이미 방문, 2 : 빈칸,
    # 배추의 위치 표시
    for _ in range(K):
        c,r = map(int,input().split())
        maps[r][c] = 0
    result = 0
    for i in range(N):
        for j in range(M):
            if not maps[i][j]:
                result += 1
                maps[i][j] = 1
                maps = check_one_chunk(maps, i, j)

    print(result)