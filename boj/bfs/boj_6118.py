from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
# 그래프 생성
for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1) # 🔴 양 방향으로 다 넣어줘야 함

# 문제 풀이
visited = [-1] * (N+1) # 🔴 visited를 0 or cnt로만 생각해서 1번째 시작점 값 설정 고민 했는데, -1 넣어서 미방문만 if문으로 거를 수 있단걸 자각
dQ = deque()
# 첫 지점 초기화
dQ.append(1)
visited[1] = 0

while dQ:
    node = dQ.popleft()
    for next_node in graph[node]:
        if visited[next_node] == -1 :
            visited[next_node] = visited[node] + 1 # 🔴 이 부분을 생각하기 어려웠음.. 거리를 for문 바깥에서 올려야 된다고 생각했는데 리스트 값에 접근해서 하면 값도 안 변해서 해당 풀이 가능
            dQ.append(next_node)

result_dist = max(visited)
print(visited.index(result_dist), result_dist, visited.count(result_dist))