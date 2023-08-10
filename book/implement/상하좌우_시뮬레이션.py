n = int(input())
x,y = 1,1
plans = input().split()

# 🟡 L,R,U,D 에 따른 이동 방향 표현법
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획에 따라 x,y값 조정
for plan in plans:

    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 예외처리) 공간을 벗어난다.
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 실제 이동 수행
    x, y = nx, ny

print(x,y)
