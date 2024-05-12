from collections import deque
N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    node1, node2 = map(int,input().split())
    graph[node1].append(node2)

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def use_dfs_succese():
    def dfs(graph, now, visited):
        visited[now] = True
        for next in graph[now]:
            if not visited[next]:
                dfs(graph, next, visited)

    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)

    result = 0
    visited = [False] * (N + 1)
    for now in range(1, N + 1):
        if not visited[now]:
            dfs(graph, now, visited)
            result += 1

    return result

def use_bfs_fail() :
    def bfs(graph, start, visited):
        dQ = deque([start])
        visited[start] = True

        while dQ:
            now = dQ.popleft()
            for next in graph[now]:
                if not visited[next]:
                    dQ.append(next)
                    visited[next] = True

    result = 0
    visited = [False] * (N + 1)
    for i in range(1, N+1):
        if not visited[i]:
            bfs(graph, i, visited)
            result += 1
    return result

def over_time() :
    result = 0
    visited = [0] * (N+1)
    visited[0] = 1  # node 1은 없기 때문에 방문처리
    while True:
        if 0 not in visited: # 안간데가 없으면
            break
        result += 1
        start = 0
        for i in range(len(visited)):
            if visited[i] == 0:
                start = i
                break
        dQ = deque([start])
        while dQ:
            now = dQ.popleft()
            visited[now] = 1
            for next in graph[now]:
                if not visited[next]:
                    dQ.append(next)
    return result

