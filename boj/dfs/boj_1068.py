""""
그래프를 깊이 탐색 한다.
현재 노드의 다음이
    - 삭제한 노드가 아니고 방문을 안 했으면 dfs()를 새로 시작한다.
    - 만약 다음 탐색 노드가 없는 노드면 리프 노드 이므로 결과 count에 +1 해준다.
"""
import sys
input = sys.stdin.readline

def dfs(cur):
    visited[cur] = True

    is_leaf = True
    leaf_count = 0
    for nx in graph[cur]:
        if not visited[nx] and nx != remove_node:
            is_leaf = False
            leaf_count += dfs(nx)

    if is_leaf:
        return 1

    return leaf_count


N = int(input().rstrip())
node_info = list(map(int,input().split()))
root_node = -1
# 그래프 정보 입력
graph = [[] for _ in range(N)]
visited = [False] * N

for node, parent_node in enumerate(node_info):
    if parent_node == -1 :
        root_node = node
    graph[parent_node].append(node)
remove_node = int(input().rstrip())


answer = 0
if remove_node == root_node:
    print(0)
else:
    print(dfs(root_node))