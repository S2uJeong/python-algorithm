from collections import deque
# 7*7 격자판의 정보가 주어진다.
maps = [list(map(int,input().split())) for _ in range(7)]

def bfs(maps):
    visited = [[False] * 7 for _ in range(7)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    dQ = deque([(0,0,0)]) # 출발은 (0,0) 목표도착은 (6,6), 3번째 인자 : distance
    print(dQ)

    while dQ:
        br,bc,d = dQ.popleft()

        if br == 6 and bc == 6 :
            return  d

        for k in range(4):
            r = br + dr[k]
            c = bc + dc[k]

            if 0 <= r < 7 and 0 <= c < 7 and maps[r][c] == 0 and not visited[r][c]:
                visited[r][c] = True
                print(f'True visited , dis: visited[{r}][{c}] , {d}')
                dQ.append((r,c,d+1))

    return -1



print(bfs(maps))


