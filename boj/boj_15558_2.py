"""
N번째 idx 이상에 다다르면 우승
- dfs : N이 커서 시간초과 걸림, 최단 거리를 구하는 bfs가 유리함
- 방향이 3가진데, 왼쪽 오른쪽이 나뉘어져 구현하는데 if 조건문을 세우는게 까다로움
"""
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int,input().split())
left = input().rstrip()
right = input().rstrip()
maps = [[],[]]
for i in range(N):
    maps[0].append(int(left[i]))
    maps[1].append(int(right[i]))

def find_road():
    move = (1,-1,K)
    dQ = deque([(0,0,0)]) # delete_ground, crt_idx, way : {0:왼쪽}, {1:오른쪽}
    visited = [[False] * N for _ in range(2)]
    visited[0][0] = True

    while dQ:
        delete_ground, crt_idx, way = dQ.popleft()

        for k in range(len(move)):
            next_idx = crt_idx + move[k]

            if next_idx >= N :
                return True

            if k != 2 :  # 점프가 아니면
                if next_idx > delete_ground and maps[way][next_idx] == 1 and not visited[way][next_idx]:
                    dQ.append((delete_ground+1, next_idx, way))
                    visited[way][next_idx] = True
            else :
                if next_idx > delete_ground and maps[1-way][next_idx] == 1 and not visited[1-way][next_idx]:
                    dQ.append((delete_ground+1, next_idx, 1-way))
                    visited[1-way][next_idx] = True
    return False

print(int(find_road()))