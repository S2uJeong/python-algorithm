"""
입력
"""
N = int(input()) # 보드의 크기
board = [[0]*(N+1) for _ in range(N+1)] # 보드 초기화
K = int(input()) # 사과의 개수
# 사과가 있는 보드 만들기
for i in range(K):
    r,c = map(int,input().split())
    board[r][c] = 1
D = int(input()) # 제시 방향 갯수
ways = []
for _ in range(D):
    s,d = input().split()
    ways.append((int(s),d))

"""
방향 회전 
"""
# 처음에 오른쪽을 보고 있으므로 (동,남,서,북)
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

"""
시뮬레이션
- board : {0:기본값}, {1:사과}, {2:뱀 존재}
"""
def simulate():
    x,y = 1,1 # 뱀의 머리 위치
    board[x][y] = 2
    direction = 0 #처음에는 동쪽을 보고 있음
    time = 0 # 시작한 뒤에 지난 '초' 시간
    index = 0 # direction index
    q = [(x,y)] # 뱀이 차지하고 있는 위치 정보
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 뱀이 갈 수 있는 길인지
        if 1 <= nx <= N and 1 <= ny <= N and board[nx][ny] != 2:
            # 사과 유무
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx,ny))
                px, py = q.pop(0)
                board[px][py] = 0
            else :
                board[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 뱀의 몸통에 부딪힘
        else:
            time += 1
            break
        x,y = nx, ny # 다음 위치로 머리를 옮긴다
        time += 1
        if index < D and time == ways[index][0] :
            direction = turn(direction, ways[index][1])
            index += 1
    return time

print(simulate())