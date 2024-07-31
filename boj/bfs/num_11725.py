"""
루트 없는 트리, 트리의 루트는 1, 각 노드의 부모 구하라.
자식을 기준으로 부모 노드를 출력해야 한다. > 어려운 점 : 입력되는 그래프가 양방향 그래프라,, 어디가 부모쪽인지 알기 어려움
"""
from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip())
graph = [[] for _ in range(N+1)]
# 그래프 정보를 입력 받아 자료에 입력
for _ in range(N-1):
    node1,node2 = map(int,input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

answer = [0] * (N+1) # idx:node, val:해당 노드의 부모노드
dQ = deque([1]) # 노드 1이 시작

# bfs라서, 시작점으로 설정한 1과 가까울 수록 먼저 탐색하게 되므로 조건문을 0일때만 update하도록 하면, 1과의 최단거리로 answer을 구성할 수 있다.
while dQ:
    now = dQ.popleft()
    for next in graph[now]:
        if answer[next] == 0 :
            answer[next] = now
            dQ.append(next)

for i in range(2,N+1):
    print(answer[i])

# bfs : 시간초과
def fail_bfs(target_child) :
    dQ = deque()
    visited = [False] * (N+1)
    # 처음 노드에 대한 초기화
    dQ.append(1) # 시작 루트가 1 부터 이므로
    visited[1] = True
    while dQ:
        node = dQ.popleft()

        for next_node in graph[node]:
            if not visited[next_node]:

                if next_node == target_child:
                    return node

                visited[next_node] = True
                dQ.append(next_node)

    return 0
def time_out_solution(N, graph):
    # 노드 2부터 bfs 메서드를 통해 부모 노드를 출력한다.
    for i in range(2,N+1):
        result = fail_bfs(i)
        print(result)