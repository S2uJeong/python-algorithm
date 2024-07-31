import sys
sys.setrecursionlimit(10**7)

# 입력받기
node, edge = map(int, input().split())

graph = [[] for _ in range(node+1)]

for _ in range(edge):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

# dfs 함수 정의
visited = [False] * (node+1)
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

# 문제 해결
count = 0
for i in range(1, node + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)
