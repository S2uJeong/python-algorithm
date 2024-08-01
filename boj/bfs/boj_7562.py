from collections import deque
import sys
input = sys.stdin.readline

T = int(input().rstrip())
directs = [(-1,-2), (-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2)] # 나이트의 움직임 (r,c)

for _ in range(T):
    N = int(input().rstrip())
    crt_r, crt_c = map(int,input().split())
    target_r, target_c = map(int,input().split())

    visited = [[False] * N for _ in range(N)]
    dQ = deque([(crt_r, crt_c,0)]) # 좌표r, c, 탐색 횟수
    visited[crt_r][crt_c] = True

    while dQ :
        crt_r, crt_c, count = dQ.popleft()
        if crt_r == target_r and crt_c == target_c:
            print(count)
            break
        for d in directs:
            nr = crt_r + d[0]
            nc = crt_c + d[1]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                dQ.append((nr,nc,count+1))
                visited[nr][nc] = True


