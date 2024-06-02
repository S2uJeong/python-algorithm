h, w = map(int,input().split())
graph = [list(map(int,input())) for _ in range(h)]
result = 0
def dfs(x,y):
    if x < 0 or y < 0 or x >= h or y >= w:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        return True

    return False


for i in range(h):
    for j in range(w):
        if dfs(i,j) == True:
            result+=1

print(result)