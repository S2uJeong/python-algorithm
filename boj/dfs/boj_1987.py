"""
늘 다른 알파벳을 지나도록 한다.
좌측 상단에서 시작해서 말이 최대한 몇 칸을 지날 수 있는가

- 어느 알파벳을 사용했는지 : visited[uni('X')] 으로 확인
- 몇 칸을 진행했는지 : 경우의 수로 확인
- 각 방향대로 진행 했을 때를 dfs로 진행시킨다.
    - 종료 조건은 다음 탐색할 게 없으면
"""
import sys
input = sys.stdin.readline
def make_alpa_road(visited):
    tmp = []
    for idx, val in enumerate(visited):
        if val:
            tmp.append(chr(idx))
    return ''.join(visited)

def dfs(r, c, count):
    global result
    result = max(result, count)

    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            continue
        if not visited[ord(maps[nr][nc]) - ord('A')]:
            visited[ord(maps[nr][nc]) - ord('A')] = 1
            dfs(nr,nc,count+1)
            visited[ord(maps[nr][nc]) - ord('A')] = 0

R, C = map(int, input().split())
maps = [list(input().strip()) for _ in range(R)]

visited = [0] * 26  # 알파벳 개수만큼 선언
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
result = 0

visited[ord(maps[0][0]) - ord('A')] = 1
dfs(0,0,1)
print(result)
