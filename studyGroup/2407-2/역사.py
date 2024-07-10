"""
사건의 개수 : 1 ~ 400
전후 관계 사실 개수 : 1 ~ 50_000

모순인 경우는 없고, 모르는 경우는 있을 수 있음
result에 append할 때, memo에도 그 순서를 같이 표시해서 자체 find를 만든다.

맨 처음에 어떤 노드를 deque에 넣어 놓고 시작할지가 고민됨.
동시에 역사가 일어난 경우는 없을까?
"""
from collections import deque
N,K = map(int,input().split())


# 위상 정렬 사용 방법
def fail_at_1percent(N,K):
    memo = [0] * (N+1) # 탐색용 : input되는 사건 번호가 1부터 시작되므로 / 이후 val이 0이면 모른다로 출력할 것.
    depth = [0] * (N+1) # 위상정렬용
    dQ = deque()
    graph = [[] for _ in range(N+1)]
    for _ in range(K):
        pre, last = map(int,input().split())
        graph[pre].append(last)
        depth[last] += 1

    # deque에 처음 들어갈 노드 탐색
    for i in range(1,N+1):
        if graph[i]: # 그래프에 원소가 없으면 앞 원소라고 볼 수 없고, 언급이 안된 원소이므로 거른다.
            if not depth[i]: # depth가 0이면 선행 사건임.
                dQ.append(i)

    find_idx = 1
    while dQ:
        cur = dQ.popleft()
        memo[cur] = find_idx
        find_idx += 1
        for next in graph[cur]:
            depth[next] -= 1
            if not depth[next]:
                dQ.append(next)

    S = int(input())
    for _ in range(S):
        S,E = map(int,input().split())
        if not memo[S] or not memo[E]:
            print(0)
        elif memo[S] < memo[E]:
            print(-1)
        elif memo[E] < memo[S]:
            print(1)
