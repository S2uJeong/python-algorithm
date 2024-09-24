from itertools import permutations
from collections import deque
import sys
input = sys.stdin.readline


def fight(cur_army, selected_pattern):
    updated_army = []
    for i in range(len(cur_army)):
        updated_army.append(cur_army[i] - selected_pattern[i])  # 체력은 음수로 떨어지지 않도록
    return updated_army

def is_annihilation(cur_army):
    return all(army <= 0 for army in cur_army)

def bfs(army, patterns):
    global answer
    dQ = deque([(0,army)])
    visited = set()
    visited.add(tuple(army)) # 방문한 상태 기록

    while dQ:
        count, cur_army = dQ.popleft()
        if is_annihilation(cur_army):
            return count # 최단 경로 내뱉고 바로 종료

        # 각 패턴 적용
        for pa in patterns:
            next_army = fight(cur_army, pa)
            next_tuple = tuple(next_army)

            if next_tuple not in visited:
                visited.add(next_tuple)
                dQ.append((count+1, next_army))

damages = [9, 3, 1]
N = int(input().rstrip())
army = list(map(int, input().split()))
patterns = list(permutations(damages[:N], N))  # 데미지 패턴 순열 생성

answer = 100000  # 최소 공격 횟수 (초기값)

# BFS로 최소 횟수 탐색
result = bfs(army, patterns)

# 최종 답 출력
print(result)