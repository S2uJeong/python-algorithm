"""
효율적인 해킹
- 사소한 로직이 시간초과를 유발함. 시간 초과를 잡는것이 관건
=> 질문게시판 보니 파이썬으로 성공한 사례 없다고 하여 pypy로 제출..
"""
import time

import sys
from collections import deque
input = sys.stdin.readline

start_time = time.time()
N, M = map(int,input().split())
graph = [[] for _ in range(N+1)] # node input이 1부터 시작
for _ in range(M):
    fr, to = map(int,input().split())
    graph[to].append(fr)   # idx가 감염시, 감염되는 노드를 원소로 가짐

result = []
for start_node in range(1,N+1):
    count = 0
    dQ = deque([start_node])
    visited = [0] * (N+1)
    visited[start_node] = 1
    while dQ:
        node = dQ.popleft()
        for next in graph[node]:
            if not visited[next]:
                count += 1
                visited[next] = 1
                dQ.append(next)
    result.append(count)

max_result = max(result)
for idx,cnt in enumerate(result):
    if max_result == cnt:
        print(idx + 1 , end = ' ')