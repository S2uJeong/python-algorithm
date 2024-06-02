N,M = map(int,input().split())
maps = [list(map(int, input())) for _ in range(N)]
print(maps)
def dfs(r,c):
    if r < 0 or r >= N or c < 0 or c >= M :
        return False
    if maps[r][c] == 0:
        maps[r][c] = 1
        dfs(r-1,c)
        dfs(r+1,c)
        dfs(r,c-1)
        dfs(r,c+1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            result += 1

print(result)