# 최소 이동 칸의 개수를 세는 방법은 어떻게 알지?
# 0이면 안 가고, 1이면 가는 단순한 행태
# 오른쪽, 아래를 우선적으로 가면 되는걸까?

from collections import deque

# 입력받기
n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# 이동할 네 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >=m :
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] == graph[x][y] + 1
                queue.append((nx,ny))

    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

# BFS를 수행한 결과 출력
print(bfs(0,0))