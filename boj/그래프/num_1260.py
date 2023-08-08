from collections import deque
# 입력
node_count, edge_count, start_node = map(int, input().split())

graph = [[] for _ in range(node_count + 1)]

for _ in range(edge_count):
    node1, node2 = map(int,input().split())
    graph[node1].append(node2)
    # 🔴 오답노트 "양방향이므로 ⬇ 의 코드가 필요하다."
    graph[node2].append(node1)

# 🔴 오답노트 : 문제에서 노드의 수가 작은것의 우선순위를 주었으므로 정렬이 필요하다.
for i in graph:
    i.sort()

# dfs, bfs 정의
def dfs(graph,visited,v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v] :
        if not visited[i] :
            dfs(graph,visited, i)

def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True

    while queue :
        v = queue.popleft()
        print(v,end = ' ')
        for i in graph[v] :
            if not visited[i]:
                queue.append(i)
                visited[i] = True


visited = [False] * (node_count+1)
dfs(graph, visited,start_node)
print()

visited = [False] * (node_count+1)
bfs(graph, visited,start_node)