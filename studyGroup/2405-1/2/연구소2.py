"""
0 : 빈 칸, 1 : 벽, 2: 바이러스 놓을 수 있는 칸
연구소 크기 : ~ 2500  , 바이러스 : ~ 10
" 모든 빈 칸에 바이러스가 있게 되는 최소 시간을 출력 "
=====================================================================================
1. 바이러스를 놓을 수 있는 칸 (= val이 2인 칸) 을 찾은 다음, 첫 바이러스 갯수 만큼 조합을 구성한다.
2. 구성한 조합으로 for문을 돌리며 최소 시간을 구한다.
    - for문 안에선 bfs를 통해 바이러스를 전파 시키고, Q가 비었는데도 map에 0 (빈칸)이 있으면 INF를 반환한다.
=====================================================================================
zero_cnt 를 이용해서, data를 따로 복제 하거나 매 순간 초기화하지 않아도 되고,
마지막에 바이러스 전파가 안된 곳을 찾으려 할 필요가 없었다는게 point
"""
import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

dr = [1,-1,0,0]
dc = [0,0,-1,1]
min_val = INF = 1e9
def bfs(virus, zero_cnt):
    global min_val
    dQ = deque()
    visited = [[False for _ in range(N)] for _ in range(N)]
    # 시작점 바이러스 (M개) 전파
    for x,y in virus:
        dQ.append((x,y,0))
        visited[x][y] = True
        zero_cnt -= 1

    while dQ:
        r,c,sec = dQ.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and data[nr][nc] != 1:
                visited[nr][nc] = True
                dQ.append([nr,nc,sec+1])
                zero_cnt -= 1
    if zero_cnt == 0:
        min_val = min(min_val,sec)

# ==== solution
N, M = map(int, input().split()) # M : 초대 바이러스 수
data = [list(map(int, input().split())) for _ in range(N)]

virus_com = [] # 바이러스 시작점 조합을 담을 리스트
zero_cnt = 0 # 바이러스가 퍼질 수 있는 공간의 합을 의미한다 (0,2 포함, 1은 벽이라 미포함)

# zero_cnt 및 virus_com 값 설정
for i in range(len(data)):
    for j in range(len(data)):
        if data[i][j] == 0 :
            zero_cnt += 1
        elif data[i][j] == 2: # 바이러스를 놓을 수 있는 곳은 2의 값을 가진 곳
            virus_com.append((i,j))
            data[i][j] = 0   # 0 or 1 로 바이러스 퍼짐 가능 유무를 표현하기 위해 값 변경
            zero_cnt += 1

for virus in combinations(virus_com, M):
    #print(f"virus는 리스트 형태로 len은 M이다. = {virus}")
    bfs(virus, zero_cnt)

# 답 출력
if min_val == INF :
    print(-1)
else :
    print(min_val)