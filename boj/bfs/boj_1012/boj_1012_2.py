"""
주어진 맵 위에서 덩어리 진 구역의 개수를 센다.

함수 : 함수가 한번 시작되어 끝나면 result + 1 ,  센 곳은 0으로 표시한다.
main : 주어지는 배추의 위치 idx 리스트를 for문으로 탐색하여 함수를 실행시킨다.

이중 for문으로 전개하는게 아니라, 배추 심은 곳만 idx를 list로 받아 해당 list로 전개하여 시간 효율성을 높임
34088KB	60ms
"""
from collections import deque
import sys
input = sys.stdin.readline

def move_and_check(r,c):
    dr = [0,0,-1,1]
    dc = [-1,1,0,0]
    dQ = deque([(r,c)])
    visited[r][c] = 1

    while dQ:
        r,c = dQ.popleft()
        for k in range(len(dr)):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                dQ.append((nr,nc))
                visited[nr][nc] = 1



T = int(input().rstrip())
for _ in range(T):
    M, N, I = map(int, input().split())
    cabbage_list = []
    visited = [[1] * M for _ in range(N)] # 1: 빈땅 , 0: 배추가 있는 곳
    for _ in range(I):
        c,r = map(int,input().split())
        cabbage_list.append((r,c))
        visited[r][c] = 0

    answer = 0
    for r,c in cabbage_list:
        if not visited[r][c]:
            answer += 1
            move_and_check(r,c)

    print(answer)