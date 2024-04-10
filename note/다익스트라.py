# 주요 개념
'''
1. 필요 자료 : 노드별 최단 거리, 방문 여부, graph
2. start 노드에 대해 각 자료에 초기화 해준다.
3. 최단 거리 자료에서 제일 작은 값을 가진 노드를 탐색한다.
4. 해당 노드를 방문처리 한다.
5. 해당 노드에 대해 연결된 노드를 확인하여, 최단 거리 테이블에 있는 cost를 비교한 뒤, 더 작은 값이 구해지면 값을 교체 한다.
    ( 최단 거리 테이블은 10억정도의 최대 값으로 초기화 되어 있음)
- 매번 제일 작은 값(거리)를 가진 노드를 추출하여 탐색하므로, 한 바퀴만 돌아도 각 노드에 대해 최단 거리를 보장할 수 있다.
'''
# code
def 다익스트라(start, distance, graph, visited):
    #시작 노드에 대해서 초기화k
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now = get_최단거리(distance, visited)
        visited[now] = True
        # 현재 노드롸 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost
def get_최단거리(distance, visited):
    min_value = int(1e9)
    indx = 0 # 가장 최단 거리가 짧은 노드의 인덱스
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

# ====================== 입출력 직접 해보기
import sys
input = sys.stdin.readline
INF = int(1e9) # 10억

# 노드의 개수, 간선의 개수 입력 받기
n,m = map(int,input().split())
# 시작 노드 번호를 입력받기
start = #int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트
visited = [False] * (n+1)
# 최단거리 테이블
distance = [INF] * (n+1)

# 간선 정보 입력 받기
for _ in range(m):
    a,b,c = map(int,input().split())
    # a번 노드에서 b노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    indx = 0 # 가장 최단 거리가 짧은 노드의 인덱스
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

# 다익스트라 알고리즘
def dijkstra(start):
    #시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드롸 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF :
        print("INFINITY")
    else :
        print(distance[i])

'''
6 11
1
1 2 2
1 3 5
1 4 1 
2 3 3
2 4 2
3 2 3
3 6 5 
4 3 3
4 5 1 
5 3 1 
5 6 2
'''