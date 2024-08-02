"""
감염 컴퓨터 갯수, 그에 걸리는 시간
테스트 케이스 당, 400_000번 연산 해야 시간 초과 안 남.
노드 ~ 10_000, 간선 ~ 100_000 이므로 N(M+N)의 알고리즘 구현해야 함

그래프 너비 탐색을 하며 걸린 시간과 노드 개수를 업데이트 한다.
=> 가중치가 있는 그래프는 bfs로는 해결 못한다. 그저 연결 되어있는 구조를 보고 빠른 구조를 가져오기 떄문.
   가중치를 고려하려면 힙정렬을 이용해서 최소 시간만 고려해주는 방식으로 해야한다. ( 다익스트라 )
"""
import heapq
import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N, B, start_node = map(int,input().split())
    graph = [[] for _ in range(N+1)]  # input되는 노드의 값이 1부터 시작하므로 뒤를 넓혀 인덱스와 노드 번호를 맞춰준다.

    # 그래프는 idx가 운명을 결정하는 쪽이고, 안에 종속 배열이 해당 idx 번호의 노드에 의존하는 노드 번호이다.(노드번호, 걸리는 시간)인 튜플 형태로 넣어짐
    for _ in range(B):
        y_node, x_node, cost = map(int,input().split())
        graph[x_node].append((cost, y_node))

    # bfs 시작
    hq = []
    INF = int(1e9)
    visited = [INF] * (N+1)
    # 초기화
    heapq.heappush(hq,(0, start_node))
    visited[start_node] = 0

    while hq:
        cost, crt_node = heapq.heappop(hq)

        for next_cost, next_node in graph[crt_node]:
            if visited[next_node] > cost + next_cost:
                visited[next_node] = cost + next_cost
                heapq.heappush(hq,(cost + next_cost, next_node))

    # visited 리스트를 통해 결과 반환

    result_count = 0
    result_cost = 0
    for i in range(len(visited)):
        if visited[i] != INF :
            result_count += 1
            result_cost = max(result_cost, visited[i])

    print(result_count, result_cost)



