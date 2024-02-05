
# map , int로 받아 왔음에 주의
    # 문제에서 주어지는 map은 7*7의 크기이다. (확정크기)
maps = [list(map(int,input().split())) for _ in range(7)]

cnt = 0
dr = [-1,1,0,0]
dc = [0,0,-1,1]
def dfs(r,c):
    global cnt
    if r == 6 and c == 6:
        cnt += 1
    else :
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr <7 and 0 <= nc < 7 and maps[nr][nc] == 0:
                maps[nr][nc] = 1
                dfs(nr,nc)
                maps[nr][nc] = 0

maps[0][0] = 1
dfs(0,0)

print(cnt)