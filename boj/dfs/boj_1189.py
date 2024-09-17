"""
도착해야 하고, 거리가 맞는 경우의 수를 구하는 문제이므로 dfs로 풀이한다.

dfs(현재 위치 정보, 맵 visited 정보, 전진한 거리 수)
"""
import sys
input = sys.stdin.readline

def dfs(cur_r, cur_c, visited, dist):
    if cur_r == 0 and cur_c == C-1: # 도착 지점에 도착
        if dist == K-1 :
            return 1
        return 0

    count = 0
    visited[cur_r][cur_c] = True

    for k in range(4):
        nr = cur_r + dr[k]
        nc = cur_c + dc[k]
        if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
            count += dfs(nr, nc, visited, dist + 1)

    visited[cur_r][cur_c] = False # 백트래킹

    return count


R, C, K = map(int,input().split())
visited = [[False] * C for _ in range(R)]
for r in range(R):
    tmp = input().rstrip()
    for c in range(C):
        if tmp[c] == 'T':
            visited[r][c] = True

dr = [0,0,-1,1]
dc = [-1,1,0,0]

print(dfs(R-1,0,visited,0))