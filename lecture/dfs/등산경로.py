#1. 제일 낮고 높은 구역의 좌표를 구한다.
 #2. 1의 좌표를 이용하여 조건식을 만들어 dfs문을 만들고 처음 시작 dfs좌표를 넣는다.
N = int(input())
maps = [list(map(int,input().split())) for _ in range(N)]
dr = [-1,1,0,0]
dc = [0,0,-1,1]
visited = [[False] * N for _ in range(N)]
cnt = 0

def get_indexes(maps):
    min_val = 1e10
    max_val = -(1e10)
    indexes = [(), ()]

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            # 출발 지점
            if maps[i][j] < min_val:
                min_val = maps[i][j]
                indexes[0] = (i,j)
            # 도착 지점
            if maps[i][j] > max_val:
                max_val = maps[i][j]
                indexes[1] = (i,j)
    return indexes

def DFS(r,c):
    global cnt
    er, ec = get_indexes(maps)[1]
    # 도착지점 도착
    if r == er and c == ec:
        cnt += 1
    else:
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and maps[nr][nc] > maps[r][c]:
                visited[nr][nc] = True
                DFS(nr,nc)
                visited[nr][nc] = False


sr, sc = get_indexes(maps)[0]
# 출발지점부터 함수 시작
visited[sr][sc] = True
DFS(sr, sc)
print(cnt)




