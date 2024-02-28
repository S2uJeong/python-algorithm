a,b = map(int,input().split())

def dfs(n):
    if n % 2 != 0:
        print(n, end =' ')

    if n == b :
        return

    dfs(n+1)

dfs(a)
