"""
1. 현재 동전이 있는 위치를 표시하는 list를 [[r,c], [r2,rc]] 형식이 아닌 1차원 리스트로 [r,c,r2,c2] 생성하여 탐색이 쉬워짐
    - List.extend([r,c]) 활용
2. 0,1 값을 가진 리스트를 만들어서 if 조건문을 간단하게 만들었다.
    - 34번째 줄 참고
"""
from collections import deque
def solve():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    dQ = deque([(coins[0], coins[1], coins[2], coins[3], 0)])  # 맨 마지막은 count 역할
    while dQ:
        r1, c1, r2, c2, cnt = dQ.popleft()
        if cnt >= 10:
            break

        for k in range(4):
            is_move = [1, 1]  # 조건문에서 활용
            nr1 = r1 + dr[k]
            nc1 = c1 + dc[k]
            nr2 = r2 + dr[k]
            nc2 = c2 + dc[k]
        # 둘 다 나가는 경우 : 아예 움직이지 않음 => continue
            if not ((0 <= nr1 < N) and (0 <= nc1 < M)) and not ((0 <= nr2 < N) and (0 <= nc2 < M)):
                continue
            # 하나만 나가는 경우 (해답) => return cnt +1
            if not ((0 <= nr1 < N) and (0 <= nc1 < M)) or not ((0 <= nr2 < N) and (0 <= nc2 < M)):
                return cnt + 1
            # 둘 다 안 나가는 경우 (벽 충돌) : 만약, 둘중 하나라도 벽이 아니면 dQ.append
            if maps[nr1][nc1] == '#':
                nr1, nc1 = r1, c1
                is_move[0] = 0
            if maps[nr2][nc2] == '#':
                nr2, nc2 = r2, c2
                is_move[1] = 0
            if is_move[0] or is_move[1]:
                dQ.append((nr1, nc1, nr2, nc2, cnt + 1))

    return -1  # dQ가 빌 때까지 진행됐다면


# 입력 및 선언
N, M = map(int,input().split() )

coins = []  # 동전의 위치를 (r,c,r,c) 형태로 저장
maps = []  # 입력 받는 MAP 데이터 저장

for i in range(N):
    r_tmp = list(input())
    maps.append(r_tmp)
    for j in range(M):
        if r_tmp[j] == 'o':
            coins.extend([i, j])


result = solve()
print(result)