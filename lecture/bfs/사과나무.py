from collections import deque
import datetime

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
def solution(N,graph):
    stime = datetime.datetime.now()
    dQ = deque([])
    dQ.append((N//2, N//2, 0)) # 한 행에서 start/end 하는 열의 위치, 현재 행의 위치
    res = 0
    while dQ:
        start,end,row = dQ.popleft()
        # 1. 문제 조건에 맞는지 확인
        if row < N:
            # 2. queue에 들어 있는 위치를 토대로 graph에서 사과나무 갯수를 찾아 res에 더해준다.
            for j in range(start, end+1):
                res += graph[row][j]
            # 3. 다음 위치를 넣어준다.
            #   * 행의 위치에 따라 시작점과 끝점의 규칙이 달라진다 (다이아몬드 모양)
            if row+1 <= N//2 :
                dQ.append( (start-1, end+1, row+1) )
            else :
                dQ.append( (start+1, end-1, row+1) )
    etime = datetime.datetime.now()
    print(f'걸린시간 : {etime - stime}')
    return print(res)


def use_bfs(N,graph):
    stime = datetime.datetime.now()
    visited = [[False] * len(graph[0]) for _ in range(len(graph))]
    # 상하좌우
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    # 시작 지점  - 맨 중앙에서 시작, bfs와 dr,dc를 이용하면 다이아몬드 방향(상하좌우)으로 퍼져나간다.
    r = c = N//2
    dQ = deque([])
    visited[r][c] = True
    res = graph[r][c]
    L = 0

    while True:
        print(f'L - {L}')

        for k in range(len(dr)):
            nr = r + dr[k]
            nc = c + dc[k]
            if not visited[nr][nc] :
                visited[nr][nc] = True
                dQ.append( (nr,nc) )
        L += 1

        for _ in range(len(dQ)):
            r,c = dQ.popleft()
            print(f'graph[{r}][{c}] = {graph[r][c]} // res = {res + graph[r][c]}')
            res += graph[r][c]

        

    etime = datetime.datetime.now()
    print(f'걸린시간 : {etime - stime}')
    return print(res)


solution(N,graph)
use_bfs(N,graph)



