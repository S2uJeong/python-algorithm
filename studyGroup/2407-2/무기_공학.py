"""
강도가 최대로 되는 블럭의 합계를 구하라.
- dp로 되는지 고민하다가, 수의 범위가 작고 중복 계산 부분을 찾기 힘들어 완탐으로 하기로 결점함
=> n의 범위가 크지 않기 때문에 백트래킹으로 구한다.
- 부메랑을 0,0 부터 시작해서 만드는데 (해당 인덱스는 부메랑의 중심 기준이다.)
  열의 값이 M에 달하면 행에 1을 더하고 열을 0으로 초기화하여 아랫줄을 탐색하게 해서 N,M 까지 도달하게 한다.
- visited로 부메랑을 만드는데 쓰인 블럭을 표시하고
- 강도를 구하는게 요점이므로 강도와 인덱스를 dfs의 변수로 넣어준다.
- 종료 조건
    - 행이 N에 달하면 부메랑을 만들 수 없으므로 return 한다.
"""
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
result = 0

dr = [(-1,0),(0,1),(-1,0),(0,1)] # dr[i]의 튜플은 i번째 모양의 부메랑의 중간에서 부터의 움직임을 뜻한다.
dc = [(0,-1),(1,0),(0,1),(-1,0)]
visited = [[False] * M for _ in range(N)]
def cal_strength(r,c,pre_strength) :
    global N,M,result
    # 🔴 열, 행 다 다랐을 때 처리 순서
    if c == M :
        c = 0
        r += 1

    if r == N :
        result = max(pre_strength, result)
        return

    if not visited[r][c]:
        # 🔴 visited[r][c] = True 처리하는 위치에 따라 값이 달라짐.
        # 위치 1 : visited[r][c] = True
        for i in range(4):
            strength = pre_strength + (maps[r][c] * 2)
            tmp_idx = [(r,c)]
            can_make_boomerang = True
            for j in range(2):
                nr = r + dr[i][j]
                nc = c + dc[i][j]
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                    strength += maps[nr][nc]
                    tmp_idx.append((nr,nc))
                else :
                    can_make_boomerang = False
                    break

            if can_make_boomerang:
                for nr,nc in tmp_idx:
                    visited[nr][nc] = True  # 위치2 : visited[r][c] = True
                cal_strength(r,c+1,strength)
                for nr,nc in tmp_idx:
                    visited[nr][nc] = False

    # 🔴이거 없으면 완탐 안됨
    cal_strength(r,c+1,pre_strength)

cal_strength(0,0,0)
print(result)


