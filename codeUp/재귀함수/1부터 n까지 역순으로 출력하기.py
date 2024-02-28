K = int(input())

def dfs(n):
    print(n)
    if n == 1:
        return
    dfs(n-1)

dfs(K)