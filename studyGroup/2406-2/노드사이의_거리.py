import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    node1,node2,dist = map(int,input().split())
    graph[node1].append([node2, dist])
    graph[node2].append([node1, dist])

targets = [list(map(int,input().split())) for _ in range(M)]

for S,E in targets:
    visited = [False] * (N+1)
    dQ = deque()
    dQ.append([S,0])
    visited[S] = True
    while dQ:
        node, dist = dQ.popleft()
        if node == E :
            print(dist)
            break
        for next, n_dist in graph[node]:
            if not visited[next]:
                dQ.append([next, dist + n_dist])
                visited[next] = True


