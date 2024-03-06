"""
https://school.programmers.co.kr/learn/courses/30/lessons/43162
- dfs
"""
def solution(n, computers) :
    count = 0
    visited = [False] * n
    def dfs(v):
        visited[v] = True

        for v2 in range(n):
            if (not visited[v2]) and computers[v][v2]:
                dfs(v2)

    for node in range(n):
        if not visited[node]:
            dfs(node)
            count += 1

    return count


