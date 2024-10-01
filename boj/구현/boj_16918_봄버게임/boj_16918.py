'''
45056 KB, 5648 ms

폭탄이 있는 칸은 3초 뒤 폭발
연쇄 반응 없음
1초 : 아무것도 안 함
2초 : 폭탄이 설치 안된 곳에 모두 폭탄 설치
3초 : 이전에 설피한 폭탄 모두 폭발
4초 : 폭탄이 설치 안된 곳에 모두 폭탄 설치

결국 턴마다 빈칸, 폭탄이 번갈아가며 나타내는 오슬로같은 상황
아래 두가지를 반복
- 폭탄은 늘 설치 후 3초 후에 폭발한다. == 설치 후 3초가 경과된 폭탄을 찾아 터뜨린다. (연쇄x)
- 빈칸에 폭탄을 설치한다.

현재 초 % 3 == 설치된 초  (3 % 3 = 1) 이면 폭파시킨다.
맨 처음 시간은 0초부터 시작
빈칸이면 0으로 표시한다.
'''

N, M, S = map(int, input().split())
maps = [[] for _ in range(N)]  # 입력되는 초기 map
bomb_plant_time = [[-1] * M for _ in range(N)]  # 폭탄이 설치된 시간을 기록

for i in range(N):
    tmp = input().rstrip()
    for j in range(len(tmp)):
        maps[i].append(tmp[j])
        if tmp[j] == 'O':
            bomb_plant_time[i][j] = 0  # 초기 폭탄은 0초에 설치된 것으로 간주

dr = [0, 0, 0, 1, -1]
dc = [0, -1, 1, 0, 0]

# S초까지 시뮬레이션
for time in range(1, S + 1):
    if time % 2 == 0:
        # 폭탄을 설치한다.
        for i in range(N):
            for j in range(M):
                if maps[i][j] == '.':
                    maps[i][j] = 'O'
                    bomb_plant_time[i][j] = time
    else:
        # 폭탄을 터뜨린다.
        explosion = [] # 폭발 여부 기록
        for r in range(N):
            for c in range(M):
                if time - bomb_plant_time[r][c] == 3:
                    for k in range(5):
                        nr, nc = r + dr[k], c + dc[k]
                        if 0 <= nr < N and 0 <= nc < M:
                            explosion.append((nr,nc))

        # 폭발 적용
        while explosion:
            r,c = explosion.pop()
            maps[r][c] = '.'


for r in range(len(maps)):
    for c in range(len(maps[r])):
        print(maps[r][c], end='')
    print()
