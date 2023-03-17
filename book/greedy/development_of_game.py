map_row, map_col = map(int, input().split())
row, col, direct = map(int, input().split())

# 방문한 위치를 저장하는 맵 생성 후 0으로 초기화
d = [[0] * map_col for _ in range(map_row)]
d[row][col] = 1 # 입력받은 캐릭터의 좌표 방문 처리

# 맵을 입력 받는다.
map_list = []
for i in range(map_row):
    map_list.append(list(map(int, input().split())))

#북[0]동[1]남[2]서[3]
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 왼쪽으로만 도는 캐릭터의 습성 메서드화
def turn_left():
    global direct
    direct -= 1
    if direct == -1:
        direct = 3

count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = row + dx[direct]
    ny = col + dy[direct]
    # 회전한 이후 정면에 가보지 않은 칸이 있으면 이동
    if map_list[nx][ny] == 0 and d[nx][ny] == 0:
        d[nx][ny] == 1
        row = nx
        col = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두갈 수 없는 경우
    if turn_time == 4:
        nx = row - dx[direct]
        ny = col - dy[direct]
        # 뒤로 갈 수 있으면 이동
        if map_list[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다인 경우
        else:
            break
        turn_time = 0

print(count)

# === 아이디어 =====
#1. 왔던 길 1 표시 해서 갈 수 없는 바다를 가리키는 값과 같게 하여 다시 못 가게 처리함
#2. diraction을 dx, dy로 나눔
#3. 회전 시, 일정한 규칙이 깨지는 부분이 있는데 그걸 if문 처리해서 이어지게 함.
#4. turn_time 변수를 넣어서 4번 끝까지 도는 것을 표현함
#5. map list 와 이동 여부를 저장한 map을 따로 생성함