"""
1. 불이 전파 되는것은 경우의 수 필요 없이 일정하게 퍼져나간다.
 - 그 불이 퍼지는 매 순간,
2. while Q에 대한 break = r,c가 구석일 떄, cnt 반환  Q(r,c,cnt) / Q가 빌 때 까지 반환이 안되면 IMPOSSIBLE
3. 불이 퍼지는 걸 표현 : 해당 자리가 #이 아니면 F로 바꿔준다.
4. Q에 넣는 기준 : 다음 공간이 #이 아니고, 방문한 적이 없어야 하고, 불과 닿지 않아야 한다.
    Q에 넣은 뒤, 방문여부 체크해준다.

아이디어
1. bfs를 따로 진행하게 되어 동기화를 어떻게 하나 고민했는데, visited에 0이면 방문 아예 안 한거고, 아니면 몇번째 순서 때 해당 위치에 왔는지를 value로 넣어 비교
2. 조건식이 조금 까다로운 문제임
"""
import sys
from collections import deque
input = sys.stdin.readline

# 입력 받으면서 J,F위치 찾아주기
R,C = map(int,input().split())
data = [] # 맵을 받을 자료구조
    # bfs를 위해 각각 자료구조 생성
J_dQ = deque()
F_dQ = deque()
J_visited = [[0] * C for _ in range(R)]  # 방문기록과 cnt를 같이 이용하는 자료구조
F_visited = [[0] * C for _ in range(R)]
    # 입력 및 처음 위치 저장
for i in range(R):
    data.append(input().rstrip())
    for j in range(C):
        if data[i][j] == 'J':
            J_dQ.append((i,j))
            J_visited[i][j] = 1
        if data[i][j] == 'F':
            F_dQ.append((i,j))
            F_visited[i][j] = 1

dr = [1,-1,0,0]
dc = [0,0,-1,1]
def bfs():
    while F_dQ:
        r,c = F_dQ.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
        if 0 <= nr < R and 0 <= nc < C and not F_visited[nr][nc] and data[nr][nc] != '#':
            F_visited[nr][nc] = F_visited[r][c] + 1
            F_dQ.append((nr,nc))


    while J_dQ:
        r, c = J_dQ.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < R and 0 <= nc < C : # 바깥으로 나가지 못함 (탈출 실패)
                if data[nr][nc] != '#' and not J_visited[nr][nc] :
                    if not F_visited[nr][nc] or F_visited[nr][nc] > J_visited[r][c] + 1:  # 불과의 순서 비교
                        J_visited[nr][nc] = J_visited[r][c] + 1
                        J_dQ.append((nr,nc))
            else : # 탈출성공
                return J_visited[r][c]

    return "IMPOSSIBLE"

print(bfs())