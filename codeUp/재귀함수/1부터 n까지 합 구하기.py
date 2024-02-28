
def dfs(K) :

    if K == 1 :
        return 1
    return dfs(K-1) + K

print(dfs(int(input())))