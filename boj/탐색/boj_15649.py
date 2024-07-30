"""
1 ~ N까지 자연수 중에서 중복 없이 M개를 고른 수열
N,M은 은 8까지 가능.
"""

N,M = map(int,input().split())
result = []
def dfs(depth, tmp_result, visited):
    global result
    if depth >= M :
        for num in tmp_result:
            print(num, end=' ')
        print()
        return
    for n in range(1,N+1):
        if not visited[n]:
            tmp_result.append(n)
            visited[n] = True
            dfs(depth+1, tmp_result, visited)
            visited[n] = False
            tmp_result.pop()

visited = [False] * (N+1)
for i in range(1,N+1):
    visited[i] = True
    dfs(1, [i],visited)
    visited[i] = False