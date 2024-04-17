"""
- 제약사항
    - 노드 개수가 ~ 300,000
    - 간선 개수가 ~ 1,000,000
    - 탐색 알고리즘이 O(N) 이하 여야 한다.
- 방법
 1. 특정 도시를 시작점으로 BFS 수행
 2. 모든 도시까지의 최단 거리 계산
 3. 각 최단 거리 확인하여 그 값이 K이면 해당 도시 번호 출력
"""
import sys
from collections import deque
input = sys.stdin.readline
node_N , edge_N, target, start_node = map(int, input().split())

# 도로 정보 입력
graph = [[] for _ in range(node_N + 1)]
for _ in range(edge_N):
    s, e = map(int,input().split())
    graph[s].append(e)

# 최단 거리 초기화
distance = [-1] * (node_N + 1)
distance[start_node] = 0 # 출발 도시까지의 거리응 0

# BFS 수행
q = deque([start_node])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1 :
            distance[next_node] = distance[now]+1
            q.append(next_node)

# 최단 거리가 target인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1,node_N+1):
    if distance[i] == target:
        print(i)
        check = True
if check == False :
    print(-1)






