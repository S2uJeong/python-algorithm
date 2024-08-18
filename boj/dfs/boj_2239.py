import sys
input = sys.stdin.readline
# row, col, 3*3칸 중복여부 함수를 각각 만든다.
def check_row(fixed_r,num):
    for c in range(9):
        if num == maps[fixed_r][c]:
            return False
    return True

def check_col(fixed_c,num):
    for r in range(9):
        if num == maps[r][fixed_c]:
            return False
    return True

def chech_3by3(r,c,num):
    nr = (r//3) * 3
    nc = (c//3) * 3
    for i in range(3):
        for j in range(3):
            if num == maps[nr+i][nc+j]:
                return False
    return True

def print_maps(maps):
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            print(maps[i][j], end='')
        print()
def dfs(depth):
    if depth >= len(spaces):
        print_maps(maps)
        exit()

    nr,nc = spaces[depth]
    for num in range(1,10):
        if check_col(nc,num) and check_row(nr,num) and chech_3by3(nr,nc,num):
            maps[nr][nc] = num
            dfs(depth+1)
            maps[nr][nc] = 0

# 입력 받기, 숫자를 정해야 하는 좌표 따로 저장
maps = []
spaces = []
for r in range(9):
    tmp = list(map(int,input().rstrip()))
    for c in range(len(tmp)):
        if tmp[c] == 0:
            spaces.append((r,c))
    maps.append(tmp)

dfs(0)