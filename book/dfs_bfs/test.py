# ======= 재귀 함수 ===========
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)


print('반복적으로 구현:', factorial(5))
print('재귀적으로 구현:', factorial_recursive(5))


# ====== dfs ==========
# 그래프 - 인접리스트로 표현
graph = [[] for _ in range(3)] # 행이 3개인 2차원 리스트 초기화
graph[0].append((1,7)) # 노드 0에 연결된 노드 정보 저장 (노드, 거리)
graph[0].append((2,5))

# dfs 탐색 예제
def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

#각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)
graph = [
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
    ]

#각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * 9
#정의된 DFS 함수 호출
dfs(graph, 1, visited)
# => 1 2 7 6 8 3 4 5

# ===== bfs =======
# - dfs 보다 구현이 더 빠르게 동작한다. {dfs:스택,재귀}, {bfs:큐}
# bfs 예제
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    # 현재 노드 방문처리
    visited[start] = True
    # 큐가 빌 때 까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    # 각 노드가 방문된 정보를 리스트 자료형으로 표현
    visited = [False] * 9
    # 정의된 BFS 함수 호출
    bfs(graph, 1, visited)

