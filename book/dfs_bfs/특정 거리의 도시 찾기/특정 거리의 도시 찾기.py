"""
백준 - https://www.acmicpc.net/problem/18352
- BFS 문제
    - 문제에서 모든 도로의 거리는 1이다. 간선 비용이 1이라면 너비 우선 탐색을 이용하여 최단거리를 찾으면 된다.
"""
from collections import deque

node, edge, t_dist, start_node = map(int,input().split())
graph = [[] for _ in range(node+1)] # 문제에서 도시 번호는 1부터 시작

for _ in range(edge):
    a,b = map(int,input().split())
    graph[a].append(b)

dQ = deque([start_node])
dists = [-1] * (node+1)
dists[start_node] = 0

while dQ :
    now = dQ.popleft()
    for next_node in graph[now]:
        if dists[next_node] == -1 :
            dists[next_node] = dists[now] + 1
            dQ.append(next_node)

bool_result = False
for i,v in enumerate(dists):
    if v == t_dist:
        bool_result = True
        print(i)

if bool_result == False:
    print(-1)






