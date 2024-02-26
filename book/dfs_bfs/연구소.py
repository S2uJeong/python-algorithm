"""
https://www.acmicpc.net/problem/14502

1. 방법 선택 : 여러가지 경우의 수 중에 안전영영이 최대값이 되는 경우를 선택한다고 생각하여 dfs로 풀이
2. 자료의 수가 적으니 벽 3개를 이용한 모든 경우의 수를 살펴봐도 시간초과를 하진 않을 것이다.
   2-1. 벽을 세울 수 있는 경우의 수 : 0인 공간의 좌표를 가지고 있는 리스트를 만들어 뽑아낸다.
   2-2. 3개의 벽 경우의 수 : 2-1을 이용한 조합으로 리스트 생성
    고민사항
    삼중 for문의 함정에서 벗어날 수 없었다.
        -> 해결 방안 : graph랑 같은 크기의 이차원배열을 또 만들고, 그 배열에 벽을 세운 것을 표현
           덕분에 벽 경우의 수 자료를 탐색하는 절차 없이 graph 탐색 시, 같은 이중 for문으로 탐색 가능했음
3. 모듈화 : 바이러스 전파 함수(dfs), 안전 영역 계산 함수 =>  울타리 세울때마다 바이러스 전파하며 안전 영역 계산 (dfs)
"""

N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
graph_wall = [[0] * M for _ in range(N)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

result = 0

# 1. 바이러스 전파 함수
def virus(r,c):
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if nr >= 0 and nr < N and nc >= 0 and nc < M:
            if graph_wall[nr][nc] == 0 :
                graph_wall[nr][nc] = 2
                virus(nr,nc)

# 2. 안전영역 계산
def get_score():
    score = 0
    for i in range(N):
        for j in range(M):
            if graph_wall[i][j] == 0 :
                score += 1
    return score

# 3. 울타리 설치하며 매번 영역 크기 계산
def dfs(count):
    global result

    if count == 3 :
        for i in range(N):
            for j in range(M):
                graph_wall[i][j] = graph[i][j]

        for i in range(N):
            for j in range(M):
                if graph_wall[i][j] == 2:
                    virus(i,j)

        result = max(result,get_score())
        return

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1

dfs(0)
print(result)