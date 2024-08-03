"""
종이조각
종이를 잘라 그 위에 쓰여진 숫자를 정해진 방향에 따라 읽어 그 숫자의 합이 최대가 되도록
종이의 크기 (NxM)은 1 ~ 4
=> 종이의 크기가 작으므로, dfs로 경우의 수를 다 구해서 result를 업데이트
- 종이의 구분은 오른쪽으로 확장, 아래로 확장하는 것을 not visited && 행_열을 넘지 않는 조건으로 진행
  오른쪽 진행 (0,1), 아래 진행 (1,0) 두 경우에서 다
      - 현재 위치의 숫자를 뒤에 더할지 or 새로운 시작으로 진행할 지
      - 앞이 0으로 시작하는 경우는, 합의 최대를 만드는데 영향을 주지 않으니 pass 함으로써 시간을 줄일 수 있다.
- 종이를 자르기를 어떤 규칙으로 모든 경우의 수를 고려해서 진행해가지?
"""
import sys
input = sys.stdin.readline

def cal_sum_numList(num_list):
    digit = 1
    result = 0
    for i in range(len(num_list)-1, -1, -1) :
        result += num_list[i] * digit
        digit *= 10
    return result
def dfs(r,c, visited, countdown, sum, num_list, flag):  # flag = 0:숫자 처음부터 시작, 1:이전과 이어서
    # print(f'dfs 시작 : dfs({r},{c}, {visited}, {countdown}, {sum}, {num_list}, {flag})')
    global result
    # 현재 탐색중인 map[r][c] 결과
    if flag :
        num_list.append(maps[r][c])
    else:
        sum += cal_sum_numList(num_list)
        num_list = []
    # print(f'sum = {sum}, num_list = {num_list}')
    if countdown <= 0:  # 더 이상 진행할 map이 없다.
        result = max(sum + cal_sum_numList(num_list), result)
        # print(f'return result : {result}')
        return

    # 다음 탐색 할 것 대상으로 dfs 호출
    for dr,dc in directs:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            # print(f'다음 탐색 대상 : {nr}{nc}')
            visited[nr][nc] = True
            # 숫자를 이어간다.
            dfs(nr,nc,visited, countdown-1, sum, num_list, 1)
            # 새로운 시작을 한다.
            dfs(nr,nc,visited, countdown-1, sum, num_list, 0)

            visited[nr][nc] = False


N, M = map(int,input().split())

maps = [[] for _ in range(N)]
for i in range(N):
    string_num = input().rstrip()
    for c in string_num:
        maps[i].append(int(c))

directs = [(0,1), (1,0)]
visited = [[False] * M for _ in range(N)]
result = 0
dfs(0,0,visited,M*N,0,[],0)
print(result)

