import sys
from collections import deque
input = sys.stdin.readline

# ========== 입력 ===========
# maps 초기화 : 입력 시, 위치 idx가 1부터 들어와서 크기를 N+1로 설정
N = int(input()) # 보드 크기
maps = [[0] * (N+1) for _ in range(N+1)] # 0 : 수학, 1: 사과, 2: 뱀
A = int(input()) # 사과 개수
for _ in range(A):
    r,c = map(int,input().split())
    maps[r][c] = 1
# moves
M = int(input()) # 움직임 개수
moves = []
for _ in range(M):
    sec, way = input().split()
    moves.append((int(sec),way))


# 뱀의 늘어남을 어떻게 표시할 수 있을까? => 큐를 이용해서 앞에 넣은건 (머리) 늘리고, 뒤는 뺴는 방법 이용
# 이동하는 걸 상하좌우가 아닌 한 방향으로 방향키 누르듯 이동 하는 방법 => 왼쪽, 오른쪽 -1,+1 % 기법
def turn(direction, command):
    if command == 'L':
        return (direction - 1) % 4
    else:
        return (direction + 1) % 4

def solution():
    # 방향 : 오른쪽을 순방향으로 동(0), 남(1), 서(2), 북(3) : turn 메서드와 연관
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    # 현재 뱀의 위치
    r,c = 1,1
    maps[r][c] = 2
    snake = deque([(r,c)])

    time = 0 # 시간 : 답이랑 연관
    direction = 0 # 동쪽으로 시작
    idx = 0 # 이동 커맨드 리스트 idx
    while True:
        # 한 턴 마다 해야할 것 : 뱀 위치 옮기기(maps, snake), time 증가, time에 따른 command 확인
        nr, nc = r + dr[direction], c + dc[direction]
        # 3. time 늘리기
        time += 1
        # 1. 이동 (벽, 자기몸 충돌 시 안됨)
        if 0 < nr <= N and 0 < nc <= N and maps[nr][nc] != 2 :
            # 2. 뱀 변화
            snake.append((nr, nc))

            # 2-1. 사과가 아니면 크기가 안 늘어서 뒤를 줄여줌
            if maps[nr][nc] == 0 :
                pr,pc = snake.popleft()
                maps[pr][pc] = 0

            maps[nr][nc] = 2
            r, c = nr, nc
        else : # 1-1. 이동불가
            break
        # 4. command 확인
        if idx < M and time == moves[idx][0]: # 해당 초에 회전 커맨드가 있다. 🔴idx 관련 조건 < M 안 넣어서 index out 에러남 주의.
            direction = turn(direction, moves[idx][1])
            idx += 1

    return time

print(solution())