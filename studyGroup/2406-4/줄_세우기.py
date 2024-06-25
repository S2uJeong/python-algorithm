"""
방법1. dq와 visited 사용 => 틀렸습니다. 일부 학생의 정렬로는 문제를 풀 수 없음
1. visited[num] 으로 Q에 있는 건지 확인 (앞, 뒤 다)
2-1. 있다면 조건에 따라 앞이나 뒤로 삽입
2-2. 없다면 앞,뒤 아무데나 삽입
    예외 고민
    - 들어오는 숫자 중,
    1. 1 2 다음 2 1 같이 같은 숫자가 나온다면? = > 논리가 깨져서 이렇게 들어올 수 없음
    2. 1 2 다음 1 2  => 이미 조건에 맞춰 정렬되어 있다. continue하게 둔다. 이게 되는 이유가 조건이 있는 숫자들만 dQ로 정렬하고, 나머지 수는 그저 뒤에 나열해서 출력 할 것이라 가능

방법2. 위상 정렬 사용
"""
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)] # 숫자 입력은 1 ~ N 으로 들어오기 때문에 range(N+1)
in_degree = [0] * (N+1) # 깊이를 표현할 자료

for _ in range(M):
    nodeA, nodeB = map(int, input().split())
    graph[nodeA].append(nodeB) # 앞, 뒤가 있는 그래프므로, 한 쪽에만 담는다.
    in_degree[nodeB] += 1 # 뒤로 오는 그래프는 깊이로만 표현

dQ = deque([i for i in range(1, N+1) if in_degree[i] == 0]) # 깊이가 0인 노드를 큐에 넣는다
result = []
while dQ:
    now = dQ.popleft()
    result.append(now)
    for next in graph[now]:
        in_degree[next] -= 1
        if in_degree[next] == 0:
            dQ.append(next)

for val in result:
    print(val, end=' ')


def fail_method(N,M):
    visited = [0] * (N+1) # 숫자 입력은 1 ~ N 으로 들어오기 때문

    line = deque()
    if N == 1 :
        print(1)

    for _ in range(M):
        front, back = map(int, input().split())
        if visited[front] and visited[back]:
            continue
        elif visited[front]:
            line.append(back)
            visited[back] = 1
        elif visited[back]:
            line.appendleft(front)
            visited[front] = 1
        else:
            line.appendleft(front)
            line.append(back)
            visited[front] = 1
            visited[back] = 1

    for i in range(1,len(visited)):
        if visited[i] == 0 : # 조건에 없었던 수는 다 뒤로 넣는다.
            line.append(i)

    result = list(line)
    for val in result:
        print(val, end=' ')





