"""
. : 빈 필드, # : 울타리, o : 양, v : 늑대

울타리에 둘러 쌓인 것을 영역이라고 한다.
영역 안에 양의 수와 늑대의 수를 비교해서 더 많은 쪽이 이긴다. ( 수가 같다면 늑대가 이김 )
최종 상태의 양/늑대의 수를 출력하라.

3 <= M,N <= 250 (62,500)  , 1초
bfs로 진행 방향으로 다 담고, not dQ가 되면 세어진 양과 늑대의 수를 비교해서 결과를 리턴한다. ( 1 : 늑대 win ), ( 2 : 양 win), ( 0 : 영역에 동물 없음)

maps를 같이 사용해서, 방문했던 곳이면 '#'으로 만들어 표시한다. (방문 안하도록)

최적화 고민
- 코드를 더 함수화해서 줄일 수 있었지만, visited 배열 메모리를 더 안 쓰고 입력받은 자료를 저장하는 maps에 함꼐 visited를 표시하려고 해서 코드가 길어짐.
  그런데 파라미터를 더 쓰게 돼서, 그냥 visited를 쓰는게 나을 것 같음
  	34116	100
"""
from collections import deque
import sys

input = sys.stdin.readline


def bfs(maps, start_r, start_c, sheep, wolf):
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]
    dQ = deque([(start_r, start_c)])
    # print(f'bfs 시작 : [{start_r}][{start_c}]')
    while dQ:
        r, c = dQ.popleft()
        # 다음 경로 추가 및 방문처리
        for k in range(len(dr)):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and maps[nr][nc] != '#':
                # 수량 체크
                if maps[nr][nc] == 'o':
                    sheep += 1
                if maps[nr][nc] == 'v':
                    wolf += 1

                dQ.append((nr, nc))
                maps[nr][nc] = '#'

    # 결과 return
    if sheep == 0 and wolf == 0:
        result = (0, 0)
    elif sheep > wolf:
        result = (2, sheep)
    else:
        result = (1, wolf)

    # print(f'bfs 결과 : sheep = {sheep}, wolf = {wolf}, result = {result}')
    return result


N, M = map(int, input().split())
maps = [[] for _ in range(N)]
for i in range(N):
    string = input().rstrip()
    for c in string:
        maps[i].append(c)

sheep = 0
wolf = 0
# 시작부분 기준 정하고, visited 처리 해줘야 함
for i in range(N):
    for j in range(M):
        if maps[i][j] != '#':
            start_sheep, start_wolf = 0,0
            if maps[i][j] == 'o':
                start_sheep += 1
            if maps[i][j] == 'v':
                start_wolf += 1
            maps[i][j] = '#'
            result, count = bfs(maps, i, j, start_sheep, start_wolf)
            if result == 1:
                wolf += count
            if result == 2:
                sheep += count

print(sheep, wolf)
