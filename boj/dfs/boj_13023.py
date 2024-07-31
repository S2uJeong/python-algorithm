"""
DFS 이용하고, 깊이가 5 되면 True 반환, 안되고 끝나면 False
"""
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    n1,n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

result_flag = False
def dfs(node, depth, visited):
    global result_flag
    if depth >= 5:
        # print(f'{node}에서 depth 5 넘었음')
        result_flag = True
        return

    for next in graph[node]:
        if not visited[next]:
            # print(f'dfs({next},{depth+1}) 실행')
            visited[next] = True
            dfs(next, depth+1, visited)
            visited[next] = False   # 🔴 방문 처리를 꼭 초기화를 해주어야, 두개 이상의 노드와 관계있는 노드가 또 선택되어 경로로서 채택될 수 있음

for start_node in range(N):
    visited = [False] * N
    visited[start_node] = True
    dfs(start_node, 1, visited)
    # print(f'result_falg = {result_flag}')
    if result_flag :
        print(1)
        exit()

print(0)


