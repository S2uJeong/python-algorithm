"""
BFS를 통해 최단경로를 탐색한다.
"""
from collections import deque

S,T = input(), input()

result = 0

def bfs():
    dQ = deque([T])
    while dQ:
        cur_chars = dQ.popleft()

        if cur_chars == S : # S를 찾으면 즉시 종료
            return 1

        if len(cur_chars) == len(S): # 더 이상 줄일 수 없으면 스킵
            continue

        if cur_chars[-1] == 'A':
            dQ.append(cur_chars[:-1])

        if cur_chars[0] == 'B':
            dQ.append(cur_chars[1:][::-1])

    return 0 # 변환이 불가함.


print(bfs())